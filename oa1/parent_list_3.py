import unittest

from parent_list import LinkedList, ParentList, TwoWayList


class ParentListTests(unittest.TestCase):
    def test_hierarchy(self):
        one_way = LinkedList()
        two_way = TwoWayList()
        self.assertIsInstance(one_way, ParentList)
        self.assertIsInstance(two_way, ParentList)
        self.assertFalse(hasattr(one_way, "left"))
        self.assertTrue(callable(two_way.left))

    def test_commands(self):
        for kind in (LinkedList, TwoWayList):
            lst = kind()
            lst.add_tail(1)
            lst.add_tail(2)
            lst.add_tail(3)
            self.assertEqual(lst.get(), 1)
            self.assertTrue(lst.is_head())
            lst.tail()
            self.assertEqual(lst.get(), 3)
            lst.head()
            lst.put_right(9)
            self.assertEqual(lst.get(), 1)
            lst.right()
            self.assertEqual(lst.get(), 9)
            lst.replace(8)
            self.assertEqual(lst.get(), 8)
            lst.find(3)
            self.assertEqual(lst.get(), 3)
            lst.head()
            lst.remove_all(8)
            self.assertEqual(lst.get(), 1)
            lst.clear()
            self.assertEqual(lst.size(), 0)
            self.assertFalse(lst.is_value())

    def test_empty(self):
        for kind in (LinkedList, TwoWayList):
            lst = kind()
            lst.head()
            lst.put_right(1)
            lst.remove()
            lst.find(1)
            self.assertEqual(lst.get_head_status(), ParentList.Head.ERR)
            self.assertEqual(
                lst.get_put_right_status(), ParentList.PutRight.ERR
            )
            self.assertEqual(lst.get_remove_status(), ParentList.Remove.ERR)
            self.assertEqual(lst.get_find_status(), ParentList.Find.ERR)
            self.assertEqual(lst.size(), 0)

    def test_remove_moves_cursor(self):
        for kind in (LinkedList, TwoWayList):
            lst = kind()
            lst.add_tail(1)
            lst.add_tail(2)
            lst.add_tail(3)
            lst.right()
            lst.remove()
            self.assertEqual(lst.get(), 3)
            lst.tail()
            lst.remove()
            self.assertEqual(lst.get(), 1)

    def test_find_miss_keeps_cursor(self):
        for kind in (LinkedList, TwoWayList):
            lst = kind()
            lst.add_tail(1)
            lst.add_tail(2)
            lst.find(2)
            self.assertEqual(lst.get_find_status(), ParentList.Find.OK)
            self.assertEqual(lst.get(), 2)
            lst.find(1)
            self.assertEqual(
                lst.get_find_status(), ParentList.Find.NOT_FOUND
            )
            self.assertEqual(lst.get(), 2)

    def test_left(self):
        lst = TwoWayList()
        lst.add_tail(1)
        lst.add_tail(2)
        lst.add_tail(3)
        lst.tail()
        lst.left()
        self.assertEqual(lst.get_left_status(), TwoWayList.Left.OK)
        self.assertEqual(lst.get(), 2)
        lst.head()
        lst.left()
        self.assertEqual(lst.get_left_status(), TwoWayList.Left.ERR)
        self.assertEqual(lst.get(), 1)


if __name__ == "__main__":
    unittest.main()

