from enum import IntEnum


class DynArray:

    _MIN_CAPACITY = 16

    class Get(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Insert(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Remove(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    class Replace(IntEnum):
        NIL = 0
        OK = 1
        ERR = 2

    ## Ctor

    # post: empty array; statuses are NIL
    def __init__(self):
        self.clear()

    ## Commands

    # post: value appended
    def append(self, value):
        self._grow_if_full()
        self._array[self._count] = value
        self._count += 1

    # pre: 0 <= index <= size()
    # post: value inserted at index
    def insert(self, value, index):
        if index < 0 or index > self._count:
            self._insert_status = DynArray.Insert.ERR
        else:
            self._grow_if_full()
            for i in range(self._count, index, -1):
                self._array[i] = self._array[i - 1]
            self._array[index] = value
            self._count += 1
            self._insert_status = DynArray.Insert.OK

    # pre: 0 <= index < size()
    # post: item at index removed
    def remove(self, index):
        if index < 0 or index >= self._count:
            self._remove_status = DynArray.Remove.ERR
        else:
            for i in range(index, self._count - 1):
                self._array[i] = self._array[i + 1]
            self._count -= 1
            self._array[self._count] = None
            self._shrink()
            self._remove_status = DynArray.Remove.OK

    # pre: 0 <= index < size()
    # post: value at index replaced
    def replace(self, value, index):
        if index < 0 or index >= self._count:
            self._replace_status = DynArray.Replace.ERR
        else:
            self._array[index] = value
            self._replace_status = DynArray.Replace.OK

    # post: array is empty; statuses are NIL
    def clear(self):
        self._count = 0
        self._make_array(DynArray._MIN_CAPACITY)

        self._get_status = DynArray.Get.NIL
        self._insert_status = DynArray.Insert.NIL
        self._remove_status = DynArray.Remove.NIL
        self._replace_status = DynArray.Replace.NIL

    ## Queries

    # pre: 0 <= index < size()
    def get(self, index):
        if index < 0 or index >= self._count:
            self._get_status = DynArray.Get.ERR
            result = None
        else:
            self._get_status = DynArray.Get.OK
            result = self._array[index]
        return result

    def size(self):
        return self._count

    ## Statuses

    def get_get_status(self):
        return self._get_status

    def get_insert_status(self):
        return self._insert_status

    def get_remove_status(self):
        return self._remove_status

    def get_replace_status(self):
        return self._replace_status

    def _make_array(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._count):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def _grow_if_full(self):
        if self._count == self._capacity:
            self._make_array(self._capacity * 2)

    def _shrink(self):
        if self._capacity <= DynArray._MIN_CAPACITY:
            return
        if self._count * 2 >= self._capacity:
            return
        new_capacity = self._capacity * 2 // 3
        if new_capacity < DynArray._MIN_CAPACITY:
            new_capacity = DynArray._MIN_CAPACITY
        self._make_array(new_capacity)


