
def breath_first_search(graph, queue, node_id):
	node = graph.get_node(node_id)
	node.set_metadata('distance', 0)
	node.set_metadata('predecessor', None)
	queue.enqueue(node)
	while queue.size():
		current_node = queue.dequeue()
		for neighbor in current_node.get_neighbors():
			if not neighbor.get_metadata('color'):
				neighbor.set_metadata('color', 'white')
			if neighbor.get_metadata('color') == 'white':
				neighbor.set_metadata('color', 'grey')
				neighbor.set_metadata('distance', 
					                  current_node.get_metadata('distance')+1)
				neighbor.set_metadata('predecessor', current_node)
				queue.enqueue(neighbor)
		current_node.set_metadata('color', 'black')