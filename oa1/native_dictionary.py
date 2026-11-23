from enum import IntEnum


class NativeDictionary:

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

    class Get(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Ctor

    # pre: max_size > 0
    # post: empty dictionary; capacity() == max_size; statuses are NIL
    def __init__(self, max_size: int) -> None:
        if max_size < 1:
            max_size = 1
        self._capacity = max_size
        self.clear()

    ## Commands

    # pre: key is stored, or a free slot exists
    # post: key maps to value, size grows by one only when the key was absent
    def put(self, key: str, value: object) -> None:
        index = self._find(key)
        if index != -1:
            self._values[index] = value
            self._put_status = NativeDictionary.Put.OK
            return
        slot = self._free_slot(key)
        if slot == -1:
            self._put_status = NativeDictionary.Put.ERR
            return
        self._slots[slot] = key
        self._values[slot] = value
        self._count += 1
        self._put_status = NativeDictionary.Put.OK

    # pre: key is stored
    # post: key is not stored
    def remove(self, key: str) -> None:
        index = self._find(key)
        if index == -1:
            self._remove_status = NativeDictionary.Remove.ERR
        else:
            self._slots[index] = NativeDictionary._DELETED
            self._values[index] = None
            self._count -= 1
            self._remove_status = NativeDictionary.Remove.OK

    # post: empty dictionary; size() == 0; statuses are NIL
    def clear(self) -> None:
        self._slots: list[object] = (
            [NativeDictionary._EMPTY] * self._capacity
        )
        self._values: list[object] = [None] * self._capacity
        self._count = 0
        self._put_status = NativeDictionary.Put.NIL
        self._remove_status = NativeDictionary.Remove.NIL
        self._get_status = NativeDictionary.Get.NIL

    ## Queries

    def is_key(self, key: str) -> bool:
        return self._find(key) != -1

    def get(self, key: str) -> object:
        index = self._find(key)
        if index == -1:
            self._get_status = NativeDictionary.Get.ERR
            result = None
        else:
            self._get_status = NativeDictionary.Get.OK
            result = self._values[index]
        return result

    def size(self) -> int:
        return self._count

    def capacity(self) -> int:
        return self._capacity

    ## Statuses

    def get_put_status(self) -> int:
        return self._put_status

    def get_remove_status(self) -> int:
        return self._remove_status

    def get_get_status(self) -> int:
        return self._get_status

    def _hash(self, key: str) -> int:
        total = 0
        for character in key:
            total += ord(character)
        return total % self._capacity

    def _index(self, key: str, offset: int) -> int:
        return (self._hash(key) + offset) % self._capacity

    def _find(self, key: str) -> int:
        for offset in range(self._capacity):
            index = self._index(key, offset)
            slot = self._slots[index]
            if slot is NativeDictionary._EMPTY:
                return -1
            if slot is not NativeDictionary._DELETED and slot == key:
                return index
        return -1

    def _free_slot(self, key: str) -> int:
        found = -1
        for offset in range(self._capacity):
            index = self._index(key, offset)
            slot = self._slots[index]
            if slot is NativeDictionary._EMPTY:
                if found == -1:
                    return index
                return found
            if slot is NativeDictionary._DELETED and found == -1:
                found = index
        return found


