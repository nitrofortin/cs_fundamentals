from data_structure.array import Array

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










