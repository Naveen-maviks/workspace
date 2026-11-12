import unittest
from stack import Stack


class TestPop(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_pop_returns_the_latest_item(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.assertEqual(self.stack.pop(), "C")

    def test_pop_removes_the_latest_item(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.stack.pop()
        self.assertEqual(self.stack._items, ["A", "B"])

    def test_repeated_pop_goes_back_in_reverse_order(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        popped = [self.stack.pop(), self.stack.pop(), self.stack.pop()]
        self.assertEqual(popped, ["C", "B", "A"])
        self.assertIs(self.stack.is_empty(), True)

    def test_pop_only_item_leaves_stack_empty(self):
        self.stack.push("A")
        self.assertEqual(self.stack.pop(), "A")
        self.assertIs(self.stack.is_empty(), True)

    def test_pop_on_empty_stack_raises_clear_error(self):
        with self.assertRaises(IndexError) as context:
            self.stack.pop()
        self.assertEqual(str(context.exception), "pop from empty stack")

    def test_failed_pop_does_not_change_the_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.assertIs(self.stack.is_empty(), True)

    def test_pop_can_return_none_without_being_confused_with_empty(self):
        self.stack.push(None)
        self.assertIsNone(self.stack.pop())
        self.assertIs(self.stack.is_empty(), True)

    def test_many_pops(self):
        for i in range(100_000):
            self.stack.push(i)
        for i in reversed(range(100_000)):
            self.assertEqual(self.stack.pop(), i)
        self.assertIs(self.stack.is_empty(), True)


if __name__ == "__main__":
    unittest.main()
