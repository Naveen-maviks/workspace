import unittest
from my_list import MyList


class TestIndexOf(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def fill(self, *items):
        for item in items:
            self.tasks.append(item)

    def test_index_of_each_item(self):
        self.fill("A", "B", "C")
        for position, item in [(0, "A"), (1, "B"), (2, "C")]:
            with self.subTest(item=item):
                self.assertEqual(self.tasks.index_of(item), position)

    def test_index_of_returns_first_position_of_duplicate(self):
        self.fill("A", "B", "A")
        self.assertEqual(self.tasks.index_of("A"), 0)

    def test_index_of_missing_item_raises_clear_error(self):
        self.fill("A", "B")
        with self.assertRaises(ValueError) as context:
            self.tasks.index_of("Z")
        self.assertEqual(str(context.exception), "item not found")

    def test_index_of_on_empty_list_raises_clear_error(self):
        with self.assertRaises(ValueError) as context:
            self.tasks.index_of("A")
        self.assertEqual(str(context.exception), "item not found")

    def test_failed_index_of_does_not_change_the_list(self):
        self.fill("A", "B")
        with self.assertRaises(ValueError):
            self.tasks.index_of("Z")
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_index_of_does_not_change_the_list(self):
        self.fill("A", "B")
        self.tasks.index_of("B")
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_index_of_finds_none(self):
        self.fill("A", None)
        self.assertEqual(self.tasks.index_of(None), 1)

    def test_index_of_matches_get(self):
        self.fill("A", "B", "C")
        for item in ["A", "B", "C"]:
            with self.subTest(item=item):
                self.assertEqual(self.tasks.get(self.tasks.index_of(item)), item)

    def test_index_of_with_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertEqual(self.tasks.index_of(99_999), 99_999)
        self.assertEqual(self.tasks.index_of(0), 0)


if __name__ == "__main__":
    unittest.main()
