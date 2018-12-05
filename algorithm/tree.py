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

def pre_order_traversal_debug(node, debug):
    if debug == 20:
        raise
    if node:
        debug +=1 
        print('Visiting node {}'.format(node))
        print('Visiting node with value {}'.format(node.value))
        pre_order_traversal_debug(node.left_child, debug)
        pre_order_traversal_debug(node.right_child, debug)



def post_order_traversal(node):
    if node:
        post_order_traversal(node.left_child)
        post_order_traversal(node.right_child)
        print('Visiting node with value {}'.format(node.value))

def right_rotation(node):
    if node:
        if node.left_child:
            temp_node = node
            temp_grand_child = node.left_child.right_child

            node = node.left_child
            node.right_child = temp_node
            if temp_grand_child:
                node.right_child.left_child = temp_grand_child
    return node


def left_rotation(node):
    if node:
        if node.right_child:
            temp_node = node
            temp_grand_child = node.right_child.left_child

            node = node.right_child
            node.left_child = temp_node
            if temp_grand_child:
                node.left_child.right_child = temp_grand_child
    return node

