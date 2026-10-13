import unittest
from my_list import MyList


class TestRemoveAt(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def fill(self, *items):
        for item in items:
            self.tasks.append(item)

    def test_remove_first_item_returns_it(self):
        self.fill("A", "B", "C")
        self.assertEqual(self.tasks.remove_at(0), "A")
        self.assertEqual(self.tasks._items, ["B", "C"])

    def test_remove_middle_item_returns_it(self):
        self.fill("A", "B", "C")
        self.assertEqual(self.tasks.remove_at(1), "B")
        self.assertEqual(self.tasks._items, ["A", "C"])

    def test_remove_last_item_returns_it(self):
        self.fill("A", "B", "C")
        self.assertEqual(self.tasks.remove_at(2), "C")
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_remove_only_item_leaves_empty_list(self):
        self.fill("A")
        self.assertEqual(self.tasks.remove_at(0), "A")
        self.assertIs(self.tasks.is_empty(), True)

    def test_remove_at_each_position(self):
        cases = [
            (0, "A", ["B", "C"]),
            (1, "B", ["A", "C"]),
            (2, "C", ["A", "B"]),
        ]
        for position, removed, remaining in cases:
            with self.subTest(position=position):
                tasks = MyList()
                for item in ["A", "B", "C"]:
                    tasks.append(item)
                self.assertEqual(tasks.remove_at(position), removed)
                self.assertEqual(tasks._items, remaining)

    def test_remove_decreases_the_size(self):
        self.fill("A", "B", "C")
        self.tasks.remove_at(1)
        self.assertEqual(self.tasks.size(), 2)

    def test_later_items_shift_left(self):
        self.fill("A", "B", "C", "D")
        self.tasks.remove_at(1)
        self.assertEqual(self.tasks.get(1), "C")
        self.assertEqual(self.tasks.get(2), "D")

    def test_remove_only_the_item_at_that_position_when_duplicates(self):
        self.fill("A", "A", "B")
        self.assertEqual(self.tasks.remove_at(1), "A")
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_remove_on_empty_list_raises_clear_error(self):
        with self.assertRaises(IndexError) as context:
            self.tasks.remove_at(0)
        self.assertEqual(str(context.exception), "index out of range")

    def test_remove_position_equal_to_size_raises_clear_error(self):
        self.fill("A", "B")
        with self.assertRaises(IndexError) as context:
            self.tasks.remove_at(2)
        self.assertEqual(str(context.exception), "index out of range")

    def test_remove_negative_position_raises_clear_error(self):
        self.fill("A")
        with self.assertRaises(IndexError) as context:
            self.tasks.remove_at(-1)
        self.assertEqual(str(context.exception), "index out of range")

    def test_failed_remove_does_not_change_the_list(self):
        self.fill("A", "B")
        with self.assertRaises(IndexError):
            self.tasks.remove_at(5)
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_remove_can_return_none(self):
        self.fill(None)
        self.assertIsNone(self.tasks.remove_at(0))
        self.assertIs(self.tasks.is_empty(), True)

    def test_remove_from_the_middle_of_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertEqual(self.tasks.remove_at(50_000), 50_000)
        self.assertEqual(len(self.tasks._items), 99_999)
        self.assertEqual(self.tasks._items[50_000], 50_001)


if __name__ == "__main__":
    unittest.main()
