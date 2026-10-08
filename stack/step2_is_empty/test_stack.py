import unittest
from stack import Stack


class TestIsEmpty(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertIs(self.stack.is_empty(), True)

    def test_stack_with_one_item_is_not_empty(self):
        self.stack.push("A")
        self.assertIs(self.stack.is_empty(), False)

    def test_answer_depends_on_number_of_items(self):
        for count, expected in [(0, True), (1, False), (3, False)]:
            with self.subTest(count=count):
                stack = Stack()
                for i in range(count):
                    stack.push(i)
                self.assertIs(stack.is_empty(), expected)

    def test_checking_does_not_change_the_stack(self):
        self.stack.push("A")
        self.stack.push("B")
        self.stack.is_empty()
        self.assertEqual(self.stack._items, ["A", "B"])

    def test_many_items_is_not_empty(self):
        for i in range(100_000):
            self.stack.push(i)
        self.assertIs(self.stack.is_empty(), False)


if __name__ == "__main__":
    unittest.main()
