from enum import IntEnum


class _Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class ParentList:

    class Head(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Tail(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Right(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class PutRight(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class PutLeft(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Remove(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class AddToEmpty(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Replace(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Find(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2
        NOT_FOUND = 3

    class Get(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    # post: empty list, cursor unset, statuses NIL
    def __init__(self):
        self.clear()

    # pre: list is not empty
    # post: cursor on the first node
    def head(self):
        if self._cursor is None:
            self._head_status = ParentList.Head.ERR
        else:
            self._cursor = self._head
            self._head_status = ParentList.Head.OK

    # pre: list is not empty
    # post: cursor on the last node
    def tail(self):
        if self._cursor is None:
            self._tail_status = ParentList.Tail.ERR
        else:
            self._cursor = self._tail
            self._tail_status = ParentList.Tail.OK

    # pre: not empty, cursor not on the last node
    # post: cursor moved one node right
    def right(self):
        if self._cursor is None or self._cursor.next is None:
            self._right_status = ParentList.Right.ERR
        else:
            self._cursor = self._cursor.next
            self._right_status = ParentList.Right.OK

    # pre: list is not empty
    # post: this value inserted just after cursor; cursor stays
    def put_right(self, value):
        if self._cursor is None:
            self._put_right_status = ParentList.PutRight.ERR
        else:
            self._insert_after(self._cursor, value)
            self._put_right_status = ParentList.PutRight.OK

    # pre: list is not empty
    # post: this value inserted just before cursor; cursor stays
    def put_left(self, value):
        if self._cursor is None:
            self._put_left_status = ParentList.PutLeft.ERR
        else:
            self._insert_before(self._cursor, value)
            self._put_left_status = ParentList.PutLeft.OK

    # pre: list is not empty
    # post: current node removed; cursor to right neighbor, else left, else unset
    def remove(self):
        if self._cursor is None:
            self._remove_status = ParentList.Remove.ERR
        else:
            node = self._cursor
            right = node.next
            left = node.prev
            self._unlink(node)
            if right is not None:
                self._cursor = right
            elif left is not None:
                self._cursor = left
            else:
                self._cursor = None
            self._remove_status = ParentList.Remove.OK

    # post: empty list, cursor unset, statuses NIL
    def clear(self):
        self._head = None
        self._tail = None
        self._cursor = None
        self._size = 0

        self._head_status = ParentList.Head.NIL
        self._tail_status = ParentList.Tail.NIL
        self._right_status = ParentList.Right.NIL
        self._put_right_status = ParentList.PutRight.NIL
        self._put_left_status = ParentList.PutLeft.NIL
        self._remove_status = ParentList.Remove.NIL
        self._add_to_empty_status = ParentList.AddToEmpty.NIL
        self._replace_status = ParentList.Replace.NIL
        self._find_status = ParentList.Find.NIL
        self._get_status = ParentList.Get.NIL

    # pre: list is empty
    # post: one node with this value, cursor on it
    def add_to_empty(self, value):
        if self._cursor is not None:
            self._add_to_empty_status = ParentList.AddToEmpty.ERR
        else:
            self._make_only(value)
            self._add_to_empty_status = ParentList.AddToEmpty.OK

    # post: tail is this value; cursor on it if list was empty, else stays
    def add_tail(self, value):
        if self._cursor is None:
            self._make_only(value)
        else:
            self._insert_after(self._tail, value)

    # pre: list is not empty
    # post: current value replaced with the given one
    def replace(self, value):
        if self._cursor is None:
            self._replace_status = ParentList.Replace.ERR
        else:
            self._cursor.value = value
            self._replace_status = ParentList.Replace.OK

    # pre: list is not empty
    # post: cursor on nearest right node with this value, else stays
    def find(self, value):
        if self._cursor is None:
            self._find_status = ParentList.Find.ERR
        else:
            node = self._cursor.next
            while node is not None and node.value != value:
                node = node.next
            if node is None:
                self._find_status = ParentList.Find.NOT_FOUND
            else:
                self._cursor = node
                self._find_status = ParentList.Find.OK

    # post: no node with this value; cursor stays if kept, else nearest right, else left, else unset
    def remove_all(self, value):
        if self._cursor is not None and self._cursor.value == value:
            right = self._cursor.next
            while right is not None and right.value == value:
                right = right.next
            if right is not None:
                target = right
            else:
                left = self._cursor.prev
                while left is not None and left.value == value:
                    left = left.prev
                target = left
        else:
            target = self._cursor

        node = self._head
        while node is not None:
            nxt = node.next
            if node.value == value:
                self._unlink(node)
            node = nxt
        self._cursor = target

    # pre: list is not empty
    def get(self):
        if self._cursor is None:
            self._get_status = ParentList.Get.ERR
            result = None
        else:
            self._get_status = ParentList.Get.OK
            result = self._cursor.value
        return result

    def size(self):
        return self._size

    def is_head(self):
        return self._cursor is not None and self._cursor is self._head

    def is_tail(self):
        return self._cursor is not None and self._cursor is self._tail

    def is_value(self):
        return self._cursor is not None

    def get_head_status(self):
        return self._head_status

    def get_tail_status(self):
        return self._tail_status

    def get_right_status(self):
        return self._right_status

    def get_put_right_status(self):
        return self._put_right_status

    def get_put_left_status(self):
        return self._put_left_status

    def get_remove_status(self):
        return self._remove_status

    def get_add_to_empty_status(self):
        return self._add_to_empty_status

    def get_replace_status(self):
        return self._replace_status

    def get_find_status(self):
        return self._find_status

    def get_get_status(self):
        return self._get_status

    def _make_only(self, value):
        node = _Node(value)
        self._head = node
        self._tail = node
        self._cursor = node
        self._size = 1

    def _insert_after(self, node, value):
        fresh = _Node(value)
        fresh.prev = node
        fresh.next = node.next
        if node.next is not None:
            node.next.prev = fresh
        else:
            self._tail = fresh
        node.next = fresh
        self._size += 1

    def _insert_before(self, node, value):
        fresh = _Node(value)
        fresh.next = node
        fresh.prev = node.prev
        if node.prev is not None:
            node.prev.next = fresh
        else:
            self._head = fresh
        node.prev = fresh
        self._size += 1

    def _unlink(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        node.prev = None
        node.next = None
        self._size -= 1


class LinkedList(ParentList):
    pass


class TwoWayList(ParentList):

    class Left(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    # post: empty list, cursor unset, statuses NIL
    def clear(self):
        super().clear()
        self._left_status = TwoWayList.Left.NIL

    # pre: not empty, cursor not on the first node
    # post: cursor moved one node left
    def left(self):
        if self._cursor is None or self._cursor.prev is None:
            self._left_status = TwoWayList.Left.ERR
        else:
            self._cursor = self._cursor.prev
            self._left_status = TwoWayList.Left.OK

    def get_left_status(self):
        return self._left_status
