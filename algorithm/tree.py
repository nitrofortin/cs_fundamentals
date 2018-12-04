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

