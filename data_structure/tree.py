class TreeException(Exception):
    pass

# Utilities
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

def _tree_height(node):
    if not node:
        return 0
    return max(_tree_height(node.left_child), 
               _tree_height(node.right_child)) + 1

def _balance_factor(left_child, right_child):
    return _tree_height(left_child) - _tree_height(right_child)

# Nodes
class TreeNode:
    def __init__(self, value, **children):
        self.value = value
        self.children = children if children else {}

class BinaryTreeNode(TreeNode):
    def __init__(self, value, left_child=None, right_child=None):
        super().__init__(value, left_child=left_child, right_child=right_child)
        self.left_child = left_child
        self.right_child = right_child


# Tree templates
class Tree:
    _max_children = None
    def __init__(self, root_node=None):
        self.root_node = root_node
        if root_node:
            self._node_count = 1
        else:
            self._node_count = 0

class BinaryTree(Tree):
    _max_children = 2
    def __init__(self, root_node):
        super().__init__(root_node)


# Basic trees
class CompleteBinaryTree(BinaryTree):
    def __init__(self, root_node):
        super().__init__(root_node)
    def is_complete(self):
        return _is_complete(self.root_node)

class BinarySearchTree(BinaryTree):
    def __init__(self, root_node=None):
        super().__init__(root_node)

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
        self._node_count += 1

    def get(self, value):
        def _get(value, node):
            if not node:
                return None
            elif node.value == value:
                return node
            elif value < node.value:
                return _get(value, node.left_child)
            return _get(value, node.right_child)

        if self.root_node:
            return _get(value, self.root_node)
        return None

    def __getitem__(self, value):
        return self.get(value)

    def __contains__(self, value):
        return bool(self.get(value))

    def __len__(self):
        return self._node_count


# Binary heaps
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
        self._percolate_down_node(idx=1)       
        return old

    def _percolate_up_last_node(self):
        pass

    def _percolate_down_node(self):
        pass

    def build_heap(self):
        raise TreeException('Heap property not defined, use either `MinHeap` \
            or `MaxHeap`')

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

    def _percolate_down_node(self, idx):
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

    def _percolate_down_node(self, idx):
        while idx < self._array_repr_size:
            max_child_idx = self._get_max_child(idx)
            if self._array_repr[max_child_idx] > self._array_repr[idx]:
                self._array_repr = _swap_array_elements(self._array_repr, 
                                                        max_child_idx, 
                                                        idx)
            idx = max_child_idx

    get_max = _BinaryHeap._get_extremum
    delete_max = _BinaryHeap._delete_extremum



class AVLTreeNode(BinaryTreeNode):
    def __init__(self, 
                 value, 
                 left_child=None, 
                 right_child=None,
                 parent=None):
        super().__init__(value, left_child=left_child, right_child=right_child)
        self.parent = parent
        self.payload = None
        if left_child or right_child:
            self.balance_factor = _balance_factor(left_child, right_child)
        else:
            self.balance_factor = 0

    def _is_right_child(self):
        if self.parent:
            return self.parent.right_child == self
        return False

    def _is_left_child(self):
        if self.parent:
            return self.parent.left_child == self
        return False

    def _is_root(self):
        return not self.parent

# Self-balanced trees
class AVLTree(BinaryTree):
    def __init__(self, root_node=None):
        if not isinstance(root_node, AVLTreeNode) and root_node:
            raise TreeException(
                'Wrong type {} for `root_node`, expected AVLTreeNode' \
                .format(type(root_node)))
        super().__init__(root_node)

    def insert(self, value):
        print("Inserting node with value {}".format(value))

        def _insert(value, node):
            self.ite = 1
            if value <= node.value:
                if node.left_child:
                    _insert(value, node.left_child)
                else:
                    node.left_child = AVLTreeNode(value, parent=node)
                    self._recalculate_balance(node.left_child)
            else:
                if node.right_child:
                    try:
                        print('right child', node.right_child.value)
                        print('node', node.value)
                        print(value)
                        self.ite += 1
                        if self.ite == 10:
                            raise Exception('ite raise')
                        _insert(value, node.right_child)

                    except:
                        raise Exception('rec')
                else:
                    node.right_child = AVLTreeNode(value, parent=node)
                    self._recalculate_balance(node.right_child)
            return node
        if self.root_node:
            _insert(value, self.root_node)
        else:
            self.root_node = AVLTreeNode(value)
        self._node_count += 1

    def _recalculate_balance(self, node):
        if abs(node.balance_factor) > 1:
            self._rebalance_tree(node)
        elif node.parent:
            if node._is_left_child(): 
                node.parent.balance_factor += 1
            elif node._is_right_child(): 
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0: 
                self._recalculate_balance(node.parent)

    def _right_rotation(self, node):
        if node:
            if node.left_child:
                temp_node = node
                temp_grand_child = node.left_child.right_child
                node = node.left_child

                node.right_child = temp_node
                node.right_child.parent = node
                node.parent = temp_node.parent
                
                if temp_grand_child:
                    node.right_child.left_child = temp_grand_child
                    node.right_child.left_child.parent = node.right_child
                node.right_child.balance_factor = \
                        node.right_child.balance_factor \
                        + 1 - min(node.balance_factor, 0)
                node.balance_factor = \
                        node.balance_factor \
                        + 1 - min(node.right_child.balance_factor, 0)
        return node
        
    def _left_rotation(self, node):
        if node:
            if node.right_child:
                temp_node = node
                temp_grand_child = node.right_child.left_child

                node = node.right_child
                node.left_child = temp_node
                node.left_child.parent = node
                node.parent = temp_node.parent
                if temp_grand_child:
                    node.left_child.right_child = temp_grand_child
                    node.left_child.right_child.parent = node.left_child
                node.left_child.balance_factor = \
                        node.left_child.balance_factor \
                        + 1 - min(node.balance_factor, 0)
                node.balance_factor = \
                        node.balance_factor \
                        + 1 - min(node.left_child.balance_factor, 0)
        return node

    def _rebalance_tree(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self._right_rotation(node.right_child)
                self._left_rotation(node)
            else:
                self._right_rotation(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self._left_rotation(node.left_child)
                self._right_rotation(node)
            else:
                self._left_rotation(node)


class RedBlackTree(BinaryTree):
    pass


class SplayTree(BinaryTree):
    pass


