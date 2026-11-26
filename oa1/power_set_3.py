import unittest

from power_set import PowerSet


def filled(capacity: int, *values: object) -> PowerSet:
    result = PowerSet(capacity)
    for value in values:
        result.put(value)
    return result


class PowerSetTests(unittest.TestCase):

    def test_put_and_remove(self) -> None:
        items = PowerSet(1)
        items.put("a")
        self.assertEqual(items.size(), 1)
        self.assertEqual(items.get_put_status(), PowerSet.Put.OK)
        items.put("a")
        self.assertEqual(items.size(), 1)
        self.assertEqual(items.get_put_status(), PowerSet.Put.PRESENT)
        items.put("b")
        self.assertEqual(items.size(), 1)
        self.assertEqual(items.get_put_status(), PowerSet.Put.ERR)
        items.put("a")
        self.assertEqual(items.size(), 1)
        self.assertEqual(items.get_put_status(), PowerSet.Put.PRESENT)
        items.remove("a")
        self.assertEqual(items.size(), 0)
        items.remove("a")
        self.assertEqual(items.get_remove_status(), PowerSet.Remove.ERR)

    def test_intersection_and_difference(self) -> None:
        left = filled(4, "a", "b")
        right = filled(4, "b", "c")
        both = left.intersection(right)
        self.assertEqual(both.size(), 1)
        self.assertTrue(both.contains("b"))
        self.assertEqual(left.intersection(filled(2, "x")).size(), 0)
        self.assertEqual(left.difference(right).size(), 1)
        self.assertEqual(left.difference(left).size(), 0)
        self.assertEqual(left.size(), 2)

    def test_union(self) -> None:
        left = filled(4, "a", "b")
        merged = left.union(filled(4, "b", "c"))
        self.assertEqual(merged.size(), 3)
        self.assertTrue(merged.contains("c"))
        self.assertTrue(left.union(PowerSet(2)).equals(left))
        self.assertEqual(left.size(), 2)

    def test_subset_and_equals(self) -> None:
        current = filled(4, "a", "b")
        self.assertTrue(current.is_subset(filled(2, "a")))
        self.assertFalse(current.is_subset(filled(4, "a", "b", "c")))
        self.assertFalse(current.is_subset(filled(4, "a", "c")))
        self.assertTrue(current.equals(filled(8, "b", "a")))
        self.assertTrue(PowerSet(1).equals(PowerSet(2)))
        self.assertFalse(current.equals(filled(4, "a")))


if __name__ == "__main__":
    unittest.main()


