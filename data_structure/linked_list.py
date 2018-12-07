class LinkedListException(Exception):
    pass

class Node(object):
    def __init__(self, value, next_node, previous_node=None):
        self.value = value
        self.next_node = next_node 
        self.previous_node = previous_node

class _LinkedList(object):
    def __init__(self):
        self.last_node = None
        self.linked_list_size = 0

    def append(self, value):
        raise LinkedListException('Not implemented error')

    def _delete(self, value):
        node = self.last_node
        if node.value == value:
            return node.next_node
        while (node.next_node != None):
            if (node.next_node.value == value):
                node_delete = node.next_node
                node.next_node = node.next_node.next_node
                del node_delete
                return self.last_node
            node = node.next_node

        return self.last_node

    def delete(self, value):
        self.last_node = self._delete(value)
        self.linked_list_size -= 1
    

    def __delitem__(self, idx):
        if idx > self.linked_list_size - 1:
            raise IndexError("LinkedList index is out of bound")
        idx_node = self.last_node

        if idx == self.linked_list_size - 1:
            self.last_node = self.last_node.next_node
        else:
            pass

    def __getitem__(self, idx):
        if idx > self.linked_list_size - 1:
            raise IndexError("LinkedList index is out of bound")
        idx_node = self.last_node
        for i in range(self.linked_list_size-idx-1):
            idx_node = idx_node.next_node
        return idx_node.value

    def __contains__(self, value):
        node = self.last_node
        for i in range(self.linked_list_size):
            if node.value == value:
                return True
            node = node.next_node
        return False


class SinglyLinkedList(_LinkedList):

    def append(self, value):
        new_node = Node(value, self.last_node)
        self.last_node = new_node
        self.linked_list_size += 1


class DoublyLinkedList(_LinkedList):

    def append(self, value):
        new_node = Node(value, self.last_node)
        self.last_node.previous_node = new_node
        self.last_node = new_node
        self.linked_list_size += 1

