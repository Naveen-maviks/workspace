import unittest
from stack import Stack


class TestPush(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_first_change_is_recorded_in_empty_history(self):
        self.stack.push("A")
        self.assertEqual(self.stack._items, ["A"])

    def test_changes_are_kept_in_order(self):
        self.stack.push("A")
        self.stack.push("B")
        self.stack.push("C")
        self.assertEqual(self.stack._items, ["A", "B", "C"])

    def test_latest_change_is_last_recorded(self):
        for latest in ["C", 3, "z"]:
            with self.subTest(latest=latest):
                stack = Stack()
                stack.push("first")
                stack.push("second")
                stack.push(latest)
                self.assertEqual(stack._items[-1], latest)

    def test_earlier_changes_are_not_lost(self):
        self.stack.push("A")
        self.stack.push("B")
        self.assertEqual(self.stack._items[0], "A")
        self.assertEqual(len(self.stack._items), 2)

    def test_many_changes(self):
        for i in range(100_000):
            self.stack.push(i)
        self.assertEqual(len(self.stack._items), 100_000)
        self.assertEqual(self.stack._items[-1], 99_999)

    def test_any_value_can_be_recorded(self):
        self.stack.push(None)
        self.stack.push(0)
        self.stack.push("")
        self.assertEqual(self.stack._items, [None, 0, ""])


if __name__ == "__main__":
    unittest.main()
