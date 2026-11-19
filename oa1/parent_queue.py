from enum import IntEnum


class _Node:

    def __init__(self, value: object) -> None:
        self.value = value
        self.prev = None
        self.next = None


class ParentQueue:

    class Dequeue(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Get(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Ctor

    # post: empty queue; statuses are NIL
    def __init__(self) -> None:
        self.clear()

    ## Commands

    # post: value added at the tail
    def enqueue(self, value: object) -> None:
        self._append_tail(value)

    # pre: queue is not empty
    # post: head removed
    def dequeue(self) -> None:
        if self.size() == 0:
            self._dequeue_status = ParentQueue.Dequeue.ERR
        else:
            self._drop_head()
            self._dequeue_status = ParentQueue.Dequeue.OK

    # post: empty queue; statuses are NIL
    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
        self._dequeue_status = ParentQueue.Dequeue.NIL
        self._get_status = ParentQueue.Get.NIL

    ## Queries

    # pre: queue is not empty
    def get(self) -> object:
        if self.size() == 0:
            self._get_status = ParentQueue.Get.ERR
            result = None
        else:
            self._get_status = ParentQueue.Get.OK
            result = self._head.value
        return result

    def size(self) -> int:
        return self._size

    ## Statuses

    def get_dequeue_status(self) -> int:
        return self._dequeue_status

    def get_get_status(self) -> int:
        return self._get_status

    def _append_tail(self, value: object) -> None:
        node = _Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def _append_head(self, value: object) -> None:
        node = _Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def _drop_head(self) -> None:
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self._size -= 1

    def _drop_tail(self) -> None:
        self._tail = self._tail.prev
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        self._size -= 1


class Queue(ParentQueue):
    pass


class Deque(ParentQueue):

    class RemoveTail(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class GetTail(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Commands

    # post: value added at the head
    def add_front(self, value: object) -> None:
        self._append_head(value)

    # pre: queue is not empty
    # post: tail removed
    def remove_tail(self) -> None:
        if self.size() == 0:
            self._remove_tail_status = Deque.RemoveTail.ERR
        else:
            self._drop_tail()
            self._remove_tail_status = Deque.RemoveTail.OK

    # post: empty queue; statuses are NIL
    def clear(self) -> None:
        super().clear()
        self._remove_tail_status = Deque.RemoveTail.NIL
        self._get_tail_status = Deque.GetTail.NIL

    ## Queries

    # pre: queue is not empty
    def get_tail(self) -> object:
        if self.size() == 0:
            self._get_tail_status = Deque.GetTail.ERR
            result = None
        else:
            self._get_tail_status = Deque.GetTail.OK
            result = self._tail.value
        return result

    ## Statuses

    def get_remove_tail_status(self) -> int:
        return self._remove_tail_status

    def get_get_tail_status(self) -> int:
        return self._get_tail_status


