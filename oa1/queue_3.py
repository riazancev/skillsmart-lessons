import unittest

from queue import Queue


class QueueTests(unittest.TestCase):
    def test_empty(self) -> None:
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.NIL)
        self.assertEqual(queue.get_front_status(), Queue.Front.NIL)
        self.assertIsNone(queue.front())
        self.assertEqual(queue.get_front_status(), Queue.Front.ERR)
        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.ERR)
        self.assertEqual(queue.size(), 0)

    def test_fifo(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.front(), 1)
        self.assertEqual(queue.get_front_status(), Queue.Front.OK)
        self.assertEqual(queue.size(), 3)
        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.OK)
        self.assertEqual(queue.front(), 2)
        queue.enqueue(4)
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.front(), 4)
        self.assertEqual(queue.size(), 1)

    def test_none_value(self) -> None:
        queue = Queue()
        queue.enqueue(None)
        self.assertEqual(queue.size(), 1)
        self.assertIsNone(queue.front())
        self.assertEqual(queue.get_front_status(), Queue.Front.OK)
        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.OK)
        self.assertEqual(queue.size(), 0)

    def test_clear(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.front()
        queue.dequeue()
        queue.clear()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.NIL)
        self.assertEqual(queue.get_front_status(), Queue.Front.NIL)

    def test_failed_dequeue_keeps_order(self) -> None:
        queue = Queue()
        queue.dequeue()
        self.assertEqual(queue.get_dequeue_status(), Queue.Dequeue.ERR)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.front(), 1)
        queue.dequeue()
        self.assertEqual(queue.front(), 2)
        self.assertEqual(queue.size(), 1)


if __name__ == "__main__":
    unittest.main()


