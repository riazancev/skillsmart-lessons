from enum import IntEnum


class BoundedStack:

    class Push(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Pop(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Peek(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Ctor

    # post: capacity() > 0, stack is empty
    def __init__(self, capacity=32):
        self._capacity = max(capacity, 1)
        self.clear()

    ## Commands

    # pre: 0 <= size() < capacity()
    # post: 0 < size() <= capacity(), value added to stack
    def push(self, value):
        if self.size() < self._capacity:
            self._stack.append(value)
            self._push_status = BoundedStack.Push.OK
        else:
            self._push_status = BoundedStack.Push.ERR

    # pre: stack is not empty
    # post: top is removed from stack
    def pop(self):
        if self.size() > 0:
            self._stack.pop()
            self._pop_status = BoundedStack.Pop.OK
        else:
            self._pop_status = BoundedStack.Pop.ERR

    # post: stack is empty
    def clear(self):
        self._stack = []

        self._peek_status = BoundedStack.Peek.NIL
        self._pop_status = BoundedStack.Pop.NIL
        self._push_status = BoundedStack.Push.NIL

    ## Queries

    # pre: stack is not empty
    def peek(self):
        if self.size() > 0:
            result = self._stack[-1]
            self._peek_status = BoundedStack.Peek.OK
        else:
            result = None
            self._peek_status = BoundedStack.Peek.ERR
        return result

    def size(self):
        return len(self._stack)

    def capacity(self):
        return self._capacity

    ## Statuses

    def get_push_status(self):
        return self._push_status

    def get_pop_status(self):
        return self._pop_status

    def get_peek_status(self):
        return self._peek_status


