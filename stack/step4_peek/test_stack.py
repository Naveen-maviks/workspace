import unittest
from stack import Stack


class TestPeek(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_peek_returns_the_latest_item(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.assertEqual(self.stack.peek(), "C")

    def test_peek_does_not_remove_anything(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.stack.peek()
        self.assertEqual(self.stack._items, ["A", "B", "C"])

    def test_peek_twice_gives_the_same_answer(self):
        self.stack.push("A")
        self.stack.push("B")
        self.assertEqual(self.stack.peek(), "B")
        self.assertEqual(self.stack.peek(), "B")

    def test_peek_follows_new_pushes(self):
        self.stack.push("A")
        self.assertEqual(self.stack.peek(), "A")
        self.stack.push("B")
        self.assertEqual(self.stack.peek(), "B")

    def test_peek_after_pop_shows_the_new_top(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "B")

    def test_peek_on_empty_stack_raises_clear_error(self):
        with self.assertRaises(IndexError) as context:
            self.stack.peek()
        self.assertEqual(str(context.exception), "peek from empty stack")

    def test_failed_peek_does_not_change_the_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
        self.assertIs(self.stack.is_empty(), True)

    def test_peek_can_return_none_without_being_confused_with_empty(self):
        self.stack.push(None)
        self.assertIsNone(self.stack.peek())
        self.assertIs(self.stack.is_empty(), False)

    def test_peek_with_many_items(self):
        for i in range(100_000):
            self.stack.push(i)
        self.assertEqual(self.stack.peek(), 99_999)
        self.assertEqual(len(self.stack._items), 100_000)


if __name__ == "__main__":
    unittest.main()
