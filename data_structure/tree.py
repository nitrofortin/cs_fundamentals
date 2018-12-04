class TreeNode:
    def __init__(self, value, **children):
        self.value = value
        self.children = children if children else {}

class BinaryTreeNode(TreeNode):
    def __init__(self, value, left_child=None, right_child=None):
        super().__init__(value, left_child=left_child, right_child=right_child)
        self.left_child = left_child
        self.right_child = right_child

class Tree:
    _max_children = None
    def __init__(self, root_node=None):
        self.root_node = root_node

class BinaryTree(Tree):
    _max_children = 2
    def __init__(self, root_node):
        super().__init__(root_node)

class CompleteBinaryTree(BinaryTree):
    def __init__(self, root_node):
        super().__init__(root_node)
    def is_complete(self):
        pass

class BinarySearchTree(BinaryTree):
    def __init__(self, root_node):
        super().__init__(root_node)


class BinaryHeap(CompleteBinaryTree):
    pass

class MinHeap(BinaryHeap):
    pass

class MaxHeap(BinaryHeap):
    pass