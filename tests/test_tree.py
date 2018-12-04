import unittest

from data_structure.tree import (BinaryTreeNode, 
                                 BinaryTree, 
                                 BinarySearchTree,
                                 MinHeap,
                                 MaxHeap,
                                 _node_count,
                                 _is_complete)
from algorithm.tree import (in_order_traversal, 
                              pre_order_traversal,
                              post_order_traversal)
                              # node_count,
                              # is_complete)

def get_mock_binary_tree():
    n1 = BinaryTreeNode(1, None, None)
    n2 = BinaryTreeNode(2, None, None)
    n3 = BinaryTreeNode(3, None, None)
    n4 = BinaryTreeNode(4, None, None)
    n5 = BinaryTreeNode(5, n1, n2)
    n6 = BinaryTreeNode(6, n3, n4)
    n7 = BinaryTreeNode(7, n5, n6)
    return BinaryTree(n7)

def get_mock_binary_search_tree():
    n1 = BinaryTreeNode(7, None, None)
    return BinarySearchTree(n1)

def get_mock_min_heap():
    return get_mock_heap(MinHeap)

def get_mock_max_heap():
    return get_mock_heap(MaxHeap)

def get_mock_heap(heap_type):
    mh = heap_type()
    mh.insert(2)
    mh.insert(30)
    mh.insert(5)
    mh.insert(200)
    mh.insert(3)
    mh.insert(10)
    return mh


class TestBinaryTree(unittest.TestCase):
    def test_in_order_traversal(self):
        print("Testing in_order_traversal...")
        tree = get_mock_binary_tree()
        in_order_traversal(tree.root_node)
        print()

    def test_pre_order_traversal(self):
        print("Testing pre_order_traversal...")
        tree = get_mock_binary_tree()
        pre_order_traversal(tree.root_node)
        print()

    def test_post_order_traversal(self):
        print("Testing post_order_traversal...")
        tree = get_mock_binary_tree()
        post_order_traversal(tree.root_node)
        print()

    def test_node_count(self):
        print("Testing node_count...")
        tree = get_mock_binary_tree()
        assert(_node_count(tree.root_node)==7)  
        print()

    def test_is_complete(self):
        print("Testing is_complete...")
        tree = get_mock_binary_tree()
        assert(_is_complete(tree.root_node))  
        print()

    def test_binary_search_tree_insert(self):
        print("Testing binary_search_tree_insert...")
        binary_search_tree = get_mock_binary_search_tree()
        binary_search_tree.insert(1)
        binary_search_tree.insert(15)
        binary_search_tree.insert(3)
        binary_search_tree.insert(4)
        binary_search_tree.insert(3)
        binary_search_tree.insert(10)
        in_order_traversal(binary_search_tree.root_node)
        print()


class TestBinaryHeap(unittest.TestCase):
    def test_min_heap_get_min(self):
        print("Testing min_heap get_min")
        mh = get_mock_min_heap()
        print(mh._array_repr[1:])
        print(mh.get_min())
        print(mh._array_repr[1:])
        print()

    def test_max_heap_get_max(self):
        print("Testing min_heap get_max")
        mh = get_mock_max_heap()
        print(mh.get_max())
        print()

    def test_min_heap_get_min(self):
        print("Testing min_heap delete_min")
        mh = get_mock_min_heap()
        print(mh._array_repr[1:])
        print(mh.delete_min())
        print(mh._array_repr[1:])
        print()

    def test_max_heap_get_max(self):
        print("Testing max_heap delete_max")
        mh = get_mock_max_heap()
        print(mh._array_repr[1:])
        print(mh.delete_max())
        print(mh._array_repr[1:])
        print()