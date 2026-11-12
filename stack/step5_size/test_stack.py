import unittest
from stack import Stack


class TestSize(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_has_size_zero(self):
        self.assertEqual(self.stack.size(), 0)

    def test_size_counts_pushed_items(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.assertEqual(self.stack.size(), 3)

    def test_size_goes_down_after_pop(self):
        for item in ["A", "B", "C"]:
            self.stack.push(item)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)

    def test_size_does_not_remove_anything(self):
        self.stack.push("A")
        self.stack.push("B")
        self.stack.size()
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), "B")

    def test_size_is_zero_after_popping_everything(self):
        self.stack.push("A")
        self.stack.push("B")
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_size_counts_none_as_an_item(self):
        self.stack.push(None)
        self.assertEqual(self.stack.size(), 1)

    def test_failed_pop_does_not_change_size(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_size_with_many_items(self):
        for i in range(100_000):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), 100_000)


if __name__ == "__main__":
    unittest.main()
