import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_non_existing_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")

    def test_get_empty_array(self):
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice_full_range(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 4), [1, 2, 3, 4])

    def test_slice_partial_range(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_slice_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])

    def test_slice_negative_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], end=-1), [1, 2, 3])

    def test_slice_negative_start_and_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, -1), [3])

    def test_slice_empty_array(self):
        self.assertEqual(arrs.my_slice([], 0, 1), [])
# для коммита