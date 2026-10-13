import unittest
from my_list import MyList


class TestContains(unittest.TestCase):
    def setUp(self):
        self.tasks = MyList()

    def fill(self, *items):
        for item in items:
            self.tasks.append(item)

    def test_contains_present_item(self):
        self.fill("A", "B")
        self.assertIs(self.tasks.contains("A"), True)

    def test_contains_missing_item(self):
        self.fill("A", "B")
        self.assertIs(self.tasks.contains("C"), False)

    def test_empty_list_contains_nothing(self):
        self.assertIs(self.tasks.contains("A"), False)

    def test_contains_first_middle_and_last(self):
        self.fill("A", "B", "C")
        for item in ["A", "B", "C"]:
            with self.subTest(item=item):
                self.assertIs(self.tasks.contains(item), True)

    def test_contains_with_duplicates(self):
        self.fill("A", "A", "B")
        self.assertIs(self.tasks.contains("A"), True)

    def test_contains_none(self):
        self.assertIs(self.tasks.contains(None), False)
        self.fill(None)
        self.assertIs(self.tasks.contains(None), True)

    def test_contains_does_not_change_the_list(self):
        self.fill("A", "B")
        self.tasks.contains("A")
        self.assertEqual(self.tasks._items, ["A", "B"])

    def test_contains_returns_a_real_boolean(self):
        self.fill("A")
        self.assertIs(self.tasks.contains("A"), True)
        self.assertIs(self.tasks.contains("Z"), False)

    def test_contains_needs_an_exact_match(self):
        self.fill("a", 1)
        self.assertIs(self.tasks.contains("A"), False)
        self.assertIs(self.tasks.contains("1"), False)

    def test_contains_with_many_items(self):
        for i in range(100_000):
            self.tasks.append(i)
        self.assertIs(self.tasks.contains(99_999), True)
        self.assertIs(self.tasks.contains(-1), False)


if __name__ == "__main__":
    unittest.main()
