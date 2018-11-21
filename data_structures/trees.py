class TreeNode:
	def __init__(self, value, children=None):
		self.value = value
		self.children = children if children else []

class BinaryTreeNode(TreeNode):
	def __init__(self, value, left_child=None, right_child=None):
		super().__init__(value, [left_child, right_child])


class Tree:
	def __init__(self, root_node=None):
		self.root_node = root_node

class BinaryTree(Tree):
	def __init__(self, root_node):
		super().__init__(root_node)


def in_order_traversal(node):
	if node.value:
		
# print(BinaryTreeNode(2,3,4).children)