import unittest

from bounded_stack import BoundedStack


class BoundedStackTests(unittest.TestCase):
    def test_default_capacity(self):
        stack = BoundedStack()
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.capacity(), 32)

    def test_fixed_capacity(self):
        capacity = 42
        stack = BoundedStack(capacity)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.capacity(), capacity)

    def test_invalid_capacity(self):
        for capacity in (0, -1):
            stack = BoundedStack(capacity)
            self.assertEqual(stack.capacity(), 1)
            self.assertEqual(stack.size(), 0)

    def test_happy_path(self):
        capacity = 3
        stack = BoundedStack(capacity)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.get_push_status(), BoundedStack.Push.OK)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.get_peek_status(), BoundedStack.Peek.OK)
        stack.pop()
        self.assertEqual(stack.get_pop_status(), BoundedStack.Pop.OK)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.get_peek_status(), BoundedStack.Peek.OK)
        stack.clear()
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.capacity(), capacity)

    def test_full(self):
        capacity = 2
        stack = BoundedStack(capacity)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.get_push_status(), BoundedStack.Push.ERR)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.capacity(), capacity)

    def test_empty(self):
        capacity = 2
        stack = BoundedStack(capacity)
        stack.pop()
        self.assertEqual(stack.get_pop_status(), BoundedStack.Pop.ERR)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.get_peek_status(), BoundedStack.Peek.ERR)
        self.assertEqual(stack.size(), 0)
        self.assertEqual(stack.capacity(), capacity)


if __name__ == "__main__":
    unittest.main()


