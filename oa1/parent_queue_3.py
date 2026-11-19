import unittest

from parent_queue import Deque, ParentQueue, Queue


class ParentQueueTests(unittest.TestCase):
    def test_empty(self) -> None:
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        self.assertEqual(
            queue.get_dequeue_status(), ParentQueue.Dequeue.NIL
        )
        self.assertIsNone(queue.get())
        self.assertEqual(queue.get_get_status(), ParentQueue.Get.ERR)
        queue.dequeue()
        self.assertEqual(
            queue.get_dequeue_status(), ParentQueue.Dequeue.ERR
        )
        self.assertEqual(queue.size(), 0)

    def test_fifo(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.get(), 1)
        queue.dequeue()
        self.assertEqual(queue.get(), 2)
        queue.dequeue()
        self.assertEqual(queue.size(), 0)

    def test_deque_ends(self) -> None:
        deque = Deque()
        deque.enqueue(1)
        deque.add_front(0)
        deque.enqueue(2)
        self.assertEqual(deque.get(), 0)
        self.assertEqual(deque.get_tail(), 2)
        deque.remove_tail()
        self.assertEqual(deque.get_tail(), 1)
        self.assertEqual(deque.size(), 2)

    def test_empty_tail_and_single(self) -> None:
        deque = Deque()
        self.assertIsNone(deque.get_tail())
        self.assertEqual(deque.get_get_tail_status(), Deque.GetTail.ERR)
        deque.remove_tail()
        self.assertEqual(
            deque.get_remove_tail_status(), Deque.RemoveTail.ERR
        )
        deque.add_front(None)
        self.assertIsNone(deque.get())
        self.assertEqual(deque.get_get_status(), ParentQueue.Get.OK)
        deque.remove_tail()
        self.assertEqual(deque.size(), 0)


if __name__ == "__main__":
    unittest.main()


