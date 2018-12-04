def _node_count(node):
    if not node:
        return 0
    return (1 + _node_count(node.left_child) + _node_count(node.right_child))

def _is_complete(node):
    nb_of_nodes = _node_count(node)
    idx = 0
    def _is_comp(node, idx, nb_of_nodes):
        if not node:
            return True
        if idx >= nb_of_nodes:
            return False
        return (_is_comp(node.left_child, 2*idx+1, nb_of_nodes) and 
            _is_comp(node.right_child, 2*idx+2, nb_of_nodes))
    return _is_comp(node, idx, nb_of_nodes)

def _swap_array_elements(array, idx_1, idx_2):
    tmp = array[idx_1]
    array[idx_1] = array[idx_2]
    array[idx_2] = tmp
    return array


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


class CompleteBinaryTree(Tree):
    def __init__(self, root_node):
        super().__init__(root_node)
    def is_complete(self):
        return _is_complete(self.root_node)

class BinarySearchTree(BinaryTree):
    def __init__(self, root_node):
        super().__init__(root_node)
        self._node_count = 1

    def insert(self, value):
        print("Inserting node with value {}".format(value))
        node = BinaryTreeNode(value)
        def _insert(node, node_tree):
            if node.value < node_tree.value:
                if node_tree.left_child:
                    _insert(node, node_tree.left_child)
                else:
                    node_tree.left_child = node
            else:
                if node_tree.right_child:
                    _insert(node, node_tree.right_child)
                else:
                    node_tree.right_child = node
            return node_tree
        if self.root_node:
            _insert(node, self.root_node)
        else:
            self.root_node = node


class _BinaryHeap(CompleteBinaryTree):
    def __init__(self, root_node=None):
        super().__init__(root_node)
        self._array_repr = [0]
        self._array_repr_size = 0

    def insert(self, value):
        # Ensure shape property
        self._array_repr.append(value)
        self._array_repr_size += 1
        # Ensure heap property
        self._percolate_up_last_node()

    def _get_extremum(self):
        return self._array_repr[1]

    def _delete_extremum(self):
        old = self._array_repr[1]
        self._array_repr[1] = self._array_repr.pop()
        self._array_repr_size -= 1
        self._percolate_down_last_node()       
        return old

    def _percolate_up_last_node(self):
        pass

    def _percolate_down_last_node(self):
        pass

class MinHeap(_BinaryHeap):

    def _get_min_child(self, idx):
        if 2*idx+1 > self._array_repr_size:
            return 2*idx
        else:
            if self._array_repr[2*idx] > self._array_repr[2*idx+1]:
                return 2*idx + 1
            else:
                return 2*idx

    def _percolate_up_last_node(self):
        idx = self._array_repr_size
        while idx > 1:
            parent_idx = idx//2
            if self._array_repr[parent_idx] > self._array_repr[idx]:
                self._array_repr = _swap_array_elements(self._array_repr, 
                                                        parent_idx, 
                                                        idx)
            idx //= 2

    def _percolate_down_first_node(self):
        idx = 1
        while idx < self._array_repr_size:
            min_child_idx = self._get_min_child(idx)
            if self._array_repr[min_child_idx] < self._array_repr[idx]:
                self._array_repr = _swap_array_elements(self._array_repr, 
                                                        min_child_idx, 
                                                        idx)
            idx = min_child_idx


    get_min = _BinaryHeap._get_extremum
    delete_min = _BinaryHeap._delete_extremum



class MaxHeap(_BinaryHeap):
    def _get_max_child(self, idx):
        if 2*idx+1 > self._array_repr_size:
            return 2*idx
        else:
            if self._array_repr[2*idx] < self._array_repr[2*idx+1]:
                return 2*idx + 1
            else:
                return 2*idx

    def _percolate_up_last_node(self):
        idx = self._array_repr_size
        while idx > 1:
            parent_idx = idx//2
            if self._array_repr[parent_idx] < self._array_repr[idx]:
                self._array_repr = _swap_array_elements(self._array_repr, 
                                                        parent_idx, 
                                                        idx)
            idx //= 2

    def _percolate_down_first_node(self):
        idx = 1
        while idx < self._array_repr_size:
            max_child_idx = self._get_max_child(idx)
            if self._array_repr[max_child_idx] > self._array_repr[idx]:
                self._array_repr = _swap_array_elements(self._array_repr, 
                                                        min_child_idx, 
                                                        idx)
            idx = max_child_idx

    get_max = _BinaryHeap._get_extremum
    delete_max = _BinaryHeap._delete_extremum



class AVLTree(BinaryTree):
    pass


class RedBlackTree(BinaryTree):
    pass


class SplayTree(BinaryTree):
    pass

