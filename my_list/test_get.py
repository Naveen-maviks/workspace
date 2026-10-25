import unittest
from my_list import MyList


class TestGet(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def test_get_first_item(self):
        for item in ["A", "B", "C"]:
            self.tasks.append(item)
        self.assertEqual(self.tasks.get(0), "A")

    def test_get_last_item(self):
        for item in ["A", "B", "C"]:
            self.tasks.append(item)
        self.assertEqual(self.tasks.get(2), "C")

    def test_get_each_position(self):
        for item in ["A", "B", "C"]:
            self.tasks.append(item)
        for position, expected in [(0, "A"), (1, "B"), (2, "C")]:
            with self.subTest(position=position):
                self.assertEqual(self.tasks.get(position), expected)

    def test_get_does_not_change_the_list(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.tasks.get(0)
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_get_on_empty_list_raises_clear_error(self):
        with self.assertRaises(IndexError) as context:
            self.tasks.get(0)
        self.assertEqual(str(context.exception), "index out of range")

    def test_get_position_equal_to_size_raises_clear_error(self):
        self.tasks.append("A")
        self.tasks.append("B")
        with self.assertRaises(IndexError) as context:
            self.tasks.get(2)
        self.assertEqual(str(context.exception), "index out of range")

    def test_get_negative_position_raises_clear_error(self):
        self.tasks.append("A")
        with self.assertRaises(IndexError) as context:
            self.tasks.get(-1)
        self.assertEqual(str(context.exception), "index out of range")

    def test_failed_get_does_not_change_the_list(self):
        self.tasks.append("A")
        with self.assertRaises(IndexError):
            self.tasks.get(5)
        self.assertEqual(self.tasks._items, ["A"])

    def test_get_can_return_none(self):
        self.tasks.append(None)
        self.assertIsNone(self.tasks.get(0))

    def test_get_with_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertEqual(self.tasks.get(99_999), 99_999)
        self.assertEqual(self.tasks.get(0), 0)


if __name__ == "__main__":
    unittest.main()
