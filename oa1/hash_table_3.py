import unittest

from hash_table import HashTable


class HashTableTests(unittest.TestCase):
    def test_capacity_floor(self) -> None:
        table = HashTable(0)
        self.assertEqual(table.capacity(), 1)
        table.put(1)
        table.put(2)
        self.assertEqual(table.get_put_status(), HashTable.Put.ERR)
        self.assertTrue(table.contains(1))

    def test_empty(self) -> None:
        table = HashTable(4)
        self.assertEqual(table.size(), 0)
        self.assertEqual(table.get_put_status(), HashTable.Put.NIL)
        table.remove(1)
        self.assertEqual(table.get_remove_status(), HashTable.Remove.ERR)

    def test_membership(self) -> None:
        table = HashTable(8)
        table.put("a")
        table.put("b")
        table.put("a")
        self.assertEqual(table.size(), 2)
        table.remove("a")
        self.assertFalse(table.contains("a"))
        self.assertTrue(table.contains("b"))
        table.remove("a")
        self.assertEqual(table.get_remove_status(), HashTable.Remove.ERR)

    def test_full(self) -> None:
        table = HashTable(1)
        table.put(None)
        table.put(None)
        self.assertEqual(table.size(), 1)
        table.put(0)
        self.assertEqual(table.get_put_status(), HashTable.Put.ERR)
        self.assertTrue(table.contains(None))

    def test_collision_delete_and_clear(self) -> None:
        table = HashTable(3)
        table.put(0)
        table.put(3)
        table.put(6)
        table.remove(3)
        self.assertTrue(table.contains(0))
        self.assertFalse(table.contains(3))
        self.assertTrue(table.contains(6))
        table.clear()
        self.assertEqual(table.size(), 0)
        self.assertEqual(table.get_put_status(), HashTable.Put.NIL)


if __name__ == "__main__":
    unittest.main()


