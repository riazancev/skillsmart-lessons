import unittest

from dyn_array import DynArray


def fill(array, count):
    for i in range(count):
        array.append(i)


class DynArrayTests(unittest.TestCase):
    def test_empty(self):
        array = DynArray()
        self.assertEqual(array.size(), 0)
        self.assertEqual(array.get_get_status(), DynArray.Get.NIL)
        self.assertIsNone(array.get(0))
        self.assertEqual(array.get_get_status(), DynArray.Get.ERR)
        array.remove(0)
        self.assertEqual(array.get_remove_status(), DynArray.Remove.ERR)

    def test_append_and_replace(self):
        array = DynArray()
        array.append(1)
        array.append(2)
        self.assertEqual(array.get(0), 1)
        self.assertEqual(array.get(1), 2)
        array.replace(9, 1)
        self.assertEqual(array.get(1), 9)
        array.replace(0, 2)
        self.assertEqual(array.get_replace_status(), DynArray.Replace.ERR)
        self.assertEqual(array.get(1), 9)

    def test_insert_and_remove(self):
        array = DynArray()
        array.insert(2, 0)
        array.insert(1, 0)
        array.insert(3, array.size())
        self.assertEqual([array.get(i) for i in range(3)], [1, 2, 3])
        array.remove(1)
        self.assertEqual(array.get(0), 1)
        self.assertEqual(array.get(1), 3)
        array.insert(0, -1)
        self.assertEqual(array.get_insert_status(), DynArray.Insert.ERR)
        self.assertEqual(array.size(), 2)

    def test_clear(self):
        array = DynArray()
        fill(array, 20)
        array.clear()
        self.assertEqual(array.size(), 0)
        self.assertEqual(array._capacity, 16)
        self.assertIsNone(array.get(0))

    def test_grow_and_shrink(self):
        array = DynArray()
        fill(array, 16)
        array.append(16)
        self.assertEqual(array._capacity, 32)
        self.assertEqual(array.get(16), 16)
        array.remove(0)
        array.remove(0)
        self.assertEqual(array.size(), 15)
        self.assertEqual(array._capacity, 21)
        self.assertEqual(array.get(0), 2)


if __name__ == "__main__":
    unittest.main()

