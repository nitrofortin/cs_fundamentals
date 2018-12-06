

def show_path(results):
    results = results[::-1]
    formatted = [str(i[0])+' -> ' for i in results]
    print(''.join(formatted)[:-3])


def _get_path(node, start, key):
    results = [(node.id, node.get_metadata(key))]
    while node != start:
        node = node.get_metadata('come_from')
        results.append((node.id, node.get_metadata(key)))
    return results

def breath_first_search(graph, queue, start_id, goal_id):
    start = graph.get_node(start_id)
    goal = graph.get_node(goal_id)
    start.set_metadata('distance', 0)
    queue.enqueue(start)
    start.set_metadata('come_from', None)

    while queue.size():
        current_node = queue.dequeue()
        if current_node == goal:
            break
        for neighbor in current_node.get_neighbors():
            if not neighbor.get_metadata('color'):
                neighbor.set_metadata('color', 'white')
            if neighbor.get_metadata('color') == 'white':
                neighbor.set_metadata('color', 'grey')
                neighbor.set_metadata('distance', 
                                      current_node.get_metadata('distance') + \
                                      current_node.get_neighbor_weight(neighbor))
                neighbor.set_metadata('come_from', current_node) 
                queue.enqueue(neighbor)

    return _get_path(current_node, start, 'distance')


def dijkstra_search(graph, priority_queue, start_id, goal_id):
    start = graph.get_node(start_id)
    goal = graph.get_node(goal_id)
    start.set_metadata('cost', 0)
    priority_queue.enqueue(0, start)
    start.set_metadata('come_from', None)

    while priority_queue.size():
        current_node = priority_queue.dequeue()['payload']
        if current_node == goal:
            break
        for neighbor in current_node.get_neighbors():
            neighbor_cost = current_node.get_metadata('cost') + \
                neighbor.get_neighbor_weight(current_node)
            if (not neighbor.get_metadata('visited') or neighbor_cost < 
                neighbor.get_metadata('cost')):
                neighbor.set_metadata('cost', neighbor_cost)
                neighbor.set_metadata('come_from', current_node)
                neighbor.set_metadata('visited', True)
                priority = neighbor_cost
                priority_queue.enqueue(priority, neighbor)

    return _get_path(current_node, start, 'cost')