import unittest
from my_list import MyList


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def test_insert_at_the_start(self):
        self.tasks.append("B")
        self.tasks.append("C")
        self.tasks.insert(0, "A")
        self.assertEqual(self.tasks._items, ["A", "B", "C"])

    def test_insert_in_the_middle(self):
        self.tasks.append("A")
        self.tasks.append("C")
        self.tasks.insert(1, "B")
        self.assertEqual(self.tasks._items, ["A", "B", "C"])

    def test_insert_at_the_end(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.tasks.insert(2, "C")
        self.assertEqual(self.tasks._items, ["A", "B", "C"])

    def test_insert_into_empty_list(self):
        self.tasks.insert(0, "A")
        self.assertEqual(self.tasks._items, ["A"])

    def test_insert_at_each_position(self):
        cases = [
            (0, ["X", "A", "B"]),
            (1, ["A", "X", "B"]),
            (2, ["A", "B", "X"]),
        ]
        for position, expected in cases:
            with self.subTest(position=position):
                tasks = MyList()
                tasks.append("A")
                tasks.append("B")
                tasks.insert(position, "X")
                self.assertEqual(tasks._items, expected)

    def test_insert_increases_the_size(self):
        self.tasks.append("A")
        self.tasks.insert(0, "B")
        self.assertEqual(self.tasks.size(), 2)

    def test_insert_allows_duplicates(self):
        self.tasks.append("A")
        self.tasks.insert(0, "A")
        self.assertEqual(self.tasks._items, ["A", "A"])

    def test_insert_beyond_the_end_raises_clear_error(self):
        self.tasks.append("A")
        self.tasks.append("B")
        with self.assertRaises(IndexError) as context:
            self.tasks.insert(3, "C")
        self.assertEqual(str(context.exception), "index out of range")

    def test_insert_negative_position_raises_clear_error(self):
        self.tasks.append("A")
        with self.assertRaises(IndexError) as context:
            self.tasks.insert(-1, "B")
        self.assertEqual(str(context.exception), "index out of range")

    def test_insert_at_position_one_in_empty_list_raises_clear_error(self):
        with self.assertRaises(IndexError) as context:
            self.tasks.insert(1, "A")
        self.assertEqual(str(context.exception), "index out of range")

    def test_failed_insert_does_not_change_the_list(self):
        self.tasks.append("A")
        with self.assertRaises(IndexError):
            self.tasks.insert(5, "B")
        self.assertEqual(self.tasks._items, ["A"])

    def test_insert_accepts_none(self):
        self.tasks.append("A")
        self.tasks.insert(0, None)
        self.assertEqual(self.tasks._items, [None, "A"])

    def test_insert_in_the_middle_of_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.tasks.insert(50_000, "X")
        self.assertEqual(len(self.tasks._items), 100_001)
        self.assertEqual(self.tasks._items[50_000], "X")
        self.assertEqual(self.tasks._items[50_001], 50_000)


if __name__ == "__main__":
    unittest.main()
