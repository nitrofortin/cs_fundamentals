from data_structure.linked_list import SinglyLinkedList

l = SinglyLinkedList()

l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)

l.delete(2)

print(l.last_node.next_node.next_node)
print(l[0])