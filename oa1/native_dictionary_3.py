import unittest

from native_dictionary import NativeDictionary


class NativeDictionaryTests(unittest.TestCase):
    def test_empty(self) -> None:
        dictionary = NativeDictionary(4)
        self.assertEqual(dictionary.capacity(), 4)
        self.assertEqual(dictionary.size(), 0)
        self.assertEqual(dictionary.get_put_status(), NativeDictionary.Put.NIL)
        self.assertFalse(dictionary.is_key("a"))
        self.assertIsNone(dictionary.get("a"))
        self.assertEqual(dictionary.get_get_status(), NativeDictionary.Get.ERR)
        dictionary.remove("a")
        self.assertEqual(
            dictionary.get_remove_status(), NativeDictionary.Remove.ERR
        )
        self.assertEqual(dictionary.size(), 0)

    def test_put_new_and_existing(self) -> None:
        dictionary = NativeDictionary(4)
        dictionary.put("a", 1)
        dictionary.put("", 0)
        dictionary.put("a", 2)
        self.assertEqual(dictionary.get_put_status(), NativeDictionary.Put.OK)
        self.assertEqual(dictionary.size(), 2)
        self.assertEqual(dictionary.get("a"), 2)
        self.assertEqual(dictionary.get(""), 0)

    def test_stored_none(self) -> None:
        dictionary = NativeDictionary(4)
        dictionary.put("key", None)
        self.assertIsNone(dictionary.get("key"))
        self.assertEqual(dictionary.get_get_status(), NativeDictionary.Get.OK)
        self.assertIsNone(dictionary.get("other"))
        self.assertEqual(dictionary.get_get_status(), NativeDictionary.Get.ERR)
        self.assertTrue(dictionary.is_key("key"))

    def test_full_and_collision(self) -> None:
        dictionary = NativeDictionary(2)
        dictionary.put("ab", 1)
        dictionary.put("ba", 2)
        dictionary.put("c", 3)
        self.assertEqual(dictionary.get_put_status(), NativeDictionary.Put.ERR)
        self.assertEqual(dictionary.size(), 2)
        self.assertFalse(dictionary.is_key("c"))
        dictionary.put("ab", 9)
        self.assertEqual(dictionary.get_put_status(), NativeDictionary.Put.OK)
        self.assertEqual(dictionary.get("ab"), 9)
        dictionary.remove("ab")
        self.assertFalse(dictionary.is_key("ab"))
        self.assertEqual(dictionary.get("ba"), 2)
        self.assertEqual(dictionary.size(), 1)


if __name__ == "__main__":
    unittest.main()


