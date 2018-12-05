import unittest

from algorithm.search import (binary_search,
                              sequential_search)

def get_mock_array(N):
    return list(range(N))

class TestSearch(unittest.TestCase):
    def test_binary_search(self):
        N = 1000
        array = get_mock_array(N)
        binary_search(array, N*2)
        binary_search(array, N-1)
        binary_search(array, 1)
        binary_search(array, 0)
        binary_search(array, -N)

    def test_sequential_search(self):
        N = 1000
        array = get_mock_array(N)
        sequential_search(array, N*2)
        sequential_search(array, N-1)
        sequential_search(array, 1)
        sequential_search(array, 0)     

