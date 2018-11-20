
def get_bucket(bucket_type):
	if bucket_type == "linked_list":
		return LinkedList()
	elif bucket_type == "binary_search_tree":
		return BinarySearchTree()

class HashTable:
	def __init__(self, hashtable_size, bucket_type="linked_list"):
		self.hashtable_size = hashtable_size
		self._hashtable = Array(hashtable_size, get_bucket(bucket_type))


	def _hash_key(key):
		return hash(key)

	def _get_index(self, key):
		return _hash_key(key) % self.hashtable_size

	def __setitem__(self, key, value):
		idx = self._get_index(key)
		if value not in self._hashtable[idx]:
			self._hashtable[idx].append(value)


class Array:
	def __init__(self, array_size, placeholder=None):
		self._array = [placeholder]*array_size

	def __getitem__(self, idx):
		return self._array[idx]




class LinkedList:
	def __init__(self):
		self.last_node = None
		self.linked_list_size = 0

	def append(self, value):
		new_node = Node(value, self.last_node)
		self.last_node = new_node
		self.linked_list_size += 1

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

		# for i in range(self.linked_list_size-idx-1):
		# 	previous_node = idx_node
		# 	idx_node = idx_node.next_node
		# previous_node.next_node = idx_node.next_node


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

class BinarySearchTree:
	pass

class Node:
	def __init__(self, value, next_node):
		self.value = value
		self.next_node = next_node 


class ArrayList(list):
	def __init__(self):
		self._array = [None]
		self._array_size = 1
		self._array_iter = 0

	def append(self, value):
		if self._array_iter > len(self._array) - 1:
			self._array = self._array + [None]*self._array_size
			self._array_size = len(self._array)

		self._array[self._array_iter] = value
		self._array_iter += 1 

l = LinkedList()

l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)

l.delete(2)

print(l.last_node.next_node.next_node)
print(l[0])