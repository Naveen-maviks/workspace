import unittest
from my_list import MyList


class TestSize(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def test_new_list_has_size_zero(self):
        self.assertEqual(self.tasks.size(), 0)

    def test_size_counts_appended_items(self):
        for item in ["A", "B", "C"]:
            self.tasks.append(item)
        self.assertEqual(self.tasks.size(), 3)

    def test_size_grows_with_each_append(self):
        self.tasks.append("A")
        self.assertEqual(self.tasks.size(), 1)
        self.tasks.append("B")
        self.assertEqual(self.tasks.size(), 2)

    def test_size_does_not_change_the_list(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.tasks.size()
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_size_counts_duplicates(self):
        self.tasks.append("A")
        self.tasks.append("A")
        self.assertEqual(self.tasks.size(), 2)

    def test_size_counts_none_as_an_item(self):
        self.tasks.append(None)
        self.assertEqual(self.tasks.size(), 1)

    def test_size_with_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertEqual(self.tasks.size(), 100_000)


if __name__ == "__main__":
    unittest.main()
