# Binary tree algorithms
def in_order_traversal(node):
	if node:
		in_order_traversal(node.left_child)
		print('Visiting node with value {}'.format(node.value))
		in_order_traversal(node.right_child)

def pre_order_traversal(node):
	if node:
		print('Visiting node with value {}'.format(node.value))
		pre_order_traversal(node.left_child)
		pre_order_traversal(node.right_child)


def post_order_traversal(node):
	if node:
		post_order_traversal(node.left_child)
		post_order_traversal(node.right_child)
		print('Visiting node with value {}'.format(node.value))

def node_count(node):
	if not node:
		return 0
	return (1 + node_count(node.left_child) + node_count(node.right_child))

def is_complete(node):
	nb_of_nodes = node_count(node)
	idx = 0
	def _is_complete(node, idx, nb_of_nodes):
		if not node:
			return True
		if idx >= nb_of_nodes:
			return False
		return (_is_complete(node.left_child, 2*idx+1, nb_of_nodes) and 
			_is_complete(node.right_child, 2*idx+2, nb_of_nodes))
	return _is_complete(node, idx, nb_of_nodes)
