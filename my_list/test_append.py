import unittest
from my_list import MyList


class TestAppend(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def test_append_to_empty_list(self):
        self.tasks.append("A")
        self.assertEqual(self.tasks._items, ["A"])

    def test_append_keeps_the_order(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.tasks.append("C")
        self.assertEqual(self.tasks._items, ["A", "B", "C"])

    def test_append_does_not_change_earlier_items(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.assertEqual(self.tasks._items[0], "A")
        self.assertEqual(len(self.tasks._items), 2)

    def test_append_allows_duplicates(self):
        self.tasks.append("A")
        self.tasks.append("A")
        self.assertEqual(self.tasks._items, ["A", "A"])

    def test_append_accepts_any_value(self):
        self.tasks.append(None)
        self.tasks.append(0)
        self.tasks.append("")
        self.assertEqual(self.tasks._items, [None, 0, ""])

    def test_append_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertEqual(len(self.tasks._items), 100_000)
        self.assertEqual(self.tasks._items[-1], 99_999)


if __name__ == "__main__":
    unittest.main()
