import unittest

from data_structure.tree import MinHeap
from algorithm.sort import (heap_sort)

def get_mock_array(N):
    return list(range(N))[::-1]

class TestSort(unittest.TestCase):
    def test_heap_sort(self):
        N = 1000
        array = get_mock_array(N)
        sorted_array = heap_sort(MinHeap(), array)
        assert(array[::-1] == sorted_array)