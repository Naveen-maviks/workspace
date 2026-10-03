import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from linked_list import LinkedList


class TestRequirement1InsertAtHead(unittest.TestCase):
    def test_insert_into_empty_list(self):
        ll = LinkedList()
        ll.insert_at_head(1)
        self.assertEqual(list(ll), [1])

    def test_insert_multiple_goes_to_front(self):
        ll = LinkedList()
        ll.insert_at_head(1)
        ll.insert_at_head(2)
        self.assertEqual(list(ll), [2, 1])

import unittest
from linked_list import LinkedList


def make(*items):
    ll = LinkedList()
    for i in items:
        ll.append(i)
    return ll


class TestReq1MultipleDataTypes(unittest.TestCase):
    def test_mixed_types(self):
        ll = make(1, "two", 3.0, [4], None, True)
        self.assertEqual(list(ll), [1, "two", 3.0, [4], None, True])


class TestReq2Duplicates(unittest.TestCase):
    def test_duplicates_allowed(self):
        ll = make(5, 5, 5)
        self.assertEqual(list(ll), [5, 5, 5])
        self.assertEqual(len(ll), 3)


class TestReq3AddAnywhere(unittest.TestCase):
    def test_insert_at_head(self):
        ll = make(2, 3)
        ll.insert_at_head(1)
        self.assertEqual(list(ll), [1, 2, 3])

    def test_append_to_empty_and_non_empty(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(list(ll), [1, 2])

    def test_insert_in_between(self):
        ll = make(1, 3)
        ll.insert(1, 2)
        self.assertEqual(list(ll), [1, 2, 3])

    def test_insert_at_start_and_end_by_index(self):
        ll = make(2)
        ll.insert(0, 1)
        ll.insert(2, 3)
        self.assertEqual(list(ll), [1, 2, 3])

    def test_insert_invalid_index(self):
        ll = make(1)
        with self.assertRaises(IndexError):
            ll.insert(5, 9)
        with self.assertRaises(IndexError):
            ll.insert(-1, 9)


class TestReq4Mutable(unittest.TestCase):
    def test_set_item(self):
        ll = make(1, 2, 3)
        ll[1] = 99
        self.assertEqual(list(ll), [1, 99, 3])

    def test_set_invalid_index(self):
        with self.assertRaises(IndexError):
            make(1)[3] = 5


class TestReq5Ordered(unittest.TestCase):
    def test_order_preserved(self):
        ll = make(3, 1, 2)
        self.assertEqual(list(ll), [3, 1, 2])


class TestReq6AccessByIndex(unittest.TestCase):
    def test_get(self):
        ll = make("a", "b", "c")
        self.assertEqual(ll.get(0), "a")
        self.assertEqual(ll[2], "c")

    def test_out_of_range(self):
        ll = make(1)
        with self.assertRaises(IndexError):
            ll.get(1)
        with self.assertRaises(IndexError):
            LinkedList().get(0)


class TestReq7Length(unittest.TestCase):
    def test_length_tracks_changes(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        ll.append(1)
        ll.insert_at_head(0)
        self.assertEqual(len(ll), 2)
        ll.remove_first()
        self.assertEqual(len(ll), 1)


class TestReq8Remove(unittest.TestCase):
    def test_remove_first(self):
        ll = make(1, 2, 3)
        self.assertEqual(ll.remove_first(), 1)
        self.assertEqual(list(ll), [2, 3])

    def test_remove_last(self):
        ll = make(1, 2, 3)
        self.assertEqual(ll.remove_last(), 3)
        self.assertEqual(list(ll), [1, 2])

    def test_remove_at_middle(self):
        ll = make(1, 2, 3)
        self.assertEqual(ll.remove_at(1), 2)
        self.assertEqual(list(ll), [1, 3])

    def test_remove_only_element(self):
        ll = make(1)
        ll.remove_first()
        self.assertEqual(list(ll), [])
        self.assertIsNone(ll.head)

    def test_remove_from_empty_or_bad_index(self):
        with self.assertRaises(IndexError):
            LinkedList().remove_first()
        with self.assertRaises(IndexError):
            make(1, 2).remove_at(2)


class TestReq9Search(unittest.TestCase):
    def test_found(self):
        ll = make(10, 20, 30)
        self.assertEqual(ll.search(20), 1)
        self.assertIn(30, ll)

    def test_not_found(self):
        ll = make(1, 2)
        self.assertEqual(ll.search(9), -1)
        self.assertNotIn(9, ll)

    def test_duplicate_returns_first(self):
        self.assertEqual(make(7, 8, 7).search(7), 0)


class TestReq10Clear(unittest.TestCase):
    def test_clear(self):
        ll = make(1, 2, 3)
        ll.clear()
        self.assertEqual(len(ll), 0)
        self.assertEqual(list(ll), [])

    def test_usable_after_clear(self):
        ll = make(1, 2)
        ll.clear()
        ll.append(9)
        self.assertEqual(list(ll), [9])


class TestReq11Iterable(unittest.TestCase):
    def test_for_loop(self):
        result = [x for x in make(1, 2, 3)]
        self.assertEqual(result, [1, 2, 3])

    def test_empty_iteration(self):
        self.assertEqual(list(LinkedList()), [])

    def test_can_iterate_twice(self):
        ll = make(1, 2)
        self.assertEqual(list(ll), list(ll))


if __name__ == "__main__":
    unittest.main()
