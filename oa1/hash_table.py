from enum import IntEnum


class HashTable:

    _EMPTY = object()
    _DELETED = object()

    class Put(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Remove(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Ctor

    # pre: max_size > 0
    # post: empty table; capacity() >= 1; statuses are NIL
    def __init__(self, max_size: int) -> None:
        if max_size < 1:
            max_size = 1
        self._capacity = max_size
        self.clear()

    ## Commands

    # pre: value is already stored, or a free slot exists
    # post: value is stored
    def put(self, value: object) -> None:
        if self._find(value) != -1:
            self._put_status = HashTable.Put.OK
        else:
            index = self._free_slot(value)
            if index == -1:
                self._put_status = HashTable.Put.ERR
            else:
                self._slots[index] = value
                self._count += 1
                self._put_status = HashTable.Put.OK

    # pre: value is stored
    # post: value is not stored
    def remove(self, value: object) -> None:
        index = self._find(value)
        if index == -1:
            self._remove_status = HashTable.Remove.ERR
        else:
            self._slots[index] = HashTable._DELETED
            self._count -= 1
            self._remove_status = HashTable.Remove.OK

    # post: empty table; statuses are NIL
    def clear(self) -> None:
        self._slots = [HashTable._EMPTY] * self._capacity
        self._count = 0
        self._put_status = HashTable.Put.NIL
        self._remove_status = HashTable.Remove.NIL

    ## Queries

    # true when the value is stored
    def contains(self, value: object) -> bool:
        return self._find(value) != -1

    def size(self) -> int:
        return self._count

    def capacity(self) -> int:
        return self._capacity

    ## Statuses

    def get_put_status(self) -> int:
        return self._put_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def _index(self, value: object, offset: int) -> int:
        start = hash(value) % self._capacity
        return (start + offset) % self._capacity

    def _find(self, value: object) -> int:
        for offset in range(self._capacity):
            index = self._index(value, offset)
            item = self._slots[index]
            if item is HashTable._EMPTY:
                return -1
            if item is not HashTable._DELETED and item == value:
                return index
        return -1

    def _free_slot(self, value: object) -> int:
        found = -1
        for offset in range(self._capacity):
            index = self._index(value, offset)
            item = self._slots[index]
            if item is HashTable._EMPTY:
                if found == -1:
                    return index
                return found
            if item is HashTable._DELETED and found == -1:
                found = index
        return found


