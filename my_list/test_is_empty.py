import unittest
from my_list import MyList


class TestIsEmpty(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def test_new_list_is_empty(self):
        self.assertIs(self.tasks.is_empty(), True)

    def test_list_with_one_item_is_not_empty(self):
        self.tasks.append("A")
        self.assertIs(self.tasks.is_empty(), False)

    def test_answer_depends_on_number_of_items(self):
        for count, expected in [(0, True), (1, False), (3, False)]:
            with self.subTest(count=count):
                tasks = MyList()
                for i in range(count):
                    tasks.append(i)
                self.assertIs(tasks.is_empty(), expected)

    def test_checking_does_not_change_the_list(self):
        self.tasks.append("A")
        self.tasks.append("B")
        self.tasks.is_empty()
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_list_holding_none_is_not_empty(self):
        self.tasks.append(None)
        self.assertIs(self.tasks.is_empty(), False)

    def test_many_items_is_not_empty(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertIs(self.tasks.is_empty(), False)


if __name__ == "__main__":
    unittest.main()
