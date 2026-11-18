from enum import IntEnum


class Queue:

    class Dequeue(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2 

    class Front(IntEnum):
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
        self._items.append(value)

    # pre: queue is not empty
    # post: head removed
    def dequeue(self) -> None:
        if self.size() == 0:
            self._dequeue_status = Queue.Dequeue.ERR
        else:
            self._items.pop(0)
            self._dequeue_status = Queue.Dequeue.OK

    # post: queue is empty; statuses are NIL
    def clear(self) -> None:
        self._items = []
        self._dequeue_status = Queue.Dequeue.NIL
        self._front_status = Queue.Front.NIL

    ## Queries

    # pre: queue is not empty
    def front(self) -> object:
        if self.size() == 0:
            self._front_status = Queue.Front.ERR
            result = None
        else:
            self._front_status = Queue.Front.OK
            result = self._items[0]
        return result

    def size(self) -> int:
        return len(self._items)

    ## Statuses

    def get_dequeue_status(self) -> int:
        return self._dequeue_status

    def get_front_status(self) -> int:
        return self._front_status


