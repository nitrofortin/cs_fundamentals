import unittest

from data_structure.tree import BinaryTreeNode, BinaryTree
from algorithm.tree import (in_order_traversal, 
                              pre_order_traversal,
                              post_order_traversal,
                              node_count,
                              is_complete)

def get_mock_binary_tree():
    n1 = BinaryTreeNode(1, None, None)
    n2 = BinaryTreeNode(2, None, None)
    n3 = BinaryTreeNode(3, None, None)
    n4 = BinaryTreeNode(4, None, None)
    n5 = BinaryTreeNode(5, n1, n2)
    n6 = BinaryTreeNode(6, n3, n4)
    n7 = BinaryTreeNode(7, n5, n6)
    return BinaryTree(n7)

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
        assert(node_count(tree.root_node)==7)  
        print()

    def test_is_complete(self):
        print("Testing is_complete...")
        tree = get_mock_binary_tree()
        assert(is_complete(tree.root_node))  
        print()