class GraphException(Exception):
    pass

class GraphNode(object):
    def __init__(self, id=None):
        self.id = id
        self.neighbors = {}
        self.metadata = {}

    def add_neighbor(self, node, weight=1):
        self.neighbors[node] = weight

    def get_degree(self):
        return sum(self.neighbors.values())

    def get_neighbors(self):
        return list(self.neighbors.keys())

    def set_metadata(self, key, value):
        self.metadata[key] = value

    def get_metadata(self, key):
        if key in self.metadata:
            return self.metadata[key]
        return None

    def __contains__(self, node_id):
        return (node_id in self.neighbors.keys())



class NullNode(GraphNode):
    def __init__(self, id=None):
        self.id = None
    

class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.number_of_nodes = 0
        self._recovering_state = self

    def add_node(self, node_id):
        n = GraphNode(node_id)
        if node_id in self.nodes.keys():
            print('Node {} already exists'.format(node_id))
        else:
            self.number_of_nodes += 1
            self.nodes[node_id] = n
        
    def add_edge(self, source, target, weight=1):
        if source not in self.nodes.keys() or target not in self.nodes.keys():
            raise GraphException('Node not in graph nodes')
        node_source = self.nodes[source]
        node_target = self.nodes[target]
        node_source.add_neighbor(node_target, weight)
        node_target.add_neighbor(node_source, weight)

    def add_directed_edge(self, source, target, weight=1):
        if source not in self.nodes.keys() or target not in self.nodes.keys():
            raise GraphException('Node not in graph nodes')
        node_source = self.nodes[source]
        node_target = self.nodes[target]
        node_source.add_neighbor(node_target, weight)

    def get_node(self, node_id):
        for n in self:
            if n.id == node_id:
                return n
        return NullNode()

    def delete_node(self, node_id):
        if not node_id in self._nodes_table:
            GraphException('Node {} not found'.format(node_id))
        for n in self.nodes:
            if node_id in n:
                del n.neighbors[node_id]
        del self.nodes[node_id]

    def __contains__(self, node):
        for n in self.nodes:
            if n == node:
                return True
        return False

    def __iter__(self):
        return iter(self.nodes.values())


class GraphAdjacencyTable(object):
    def __init__(self):
        self._number_of_nodes = 0
        self._nodes_table = {}

    def add_node(self, node_id):
        if node_id not in self._nodes_table.keys():
            self._nodes_table[node_id] = {}

    def add_edge_directed(self, source_id, target_id, weight=1):
        if target_id not in self._nodes_table[source_id].keys():
            self._nodes_table[source_id] = {target_id: weight}

    def add_edge(self, node_1, node_2, weight=1):
        self.add_edge_directed(node_1, node_2)
        self.add_edge_directed(node_2, node_1)

    def delete_node(self, node_id):
        if not node_id in self._nodes_table:
            GraphException('Node {} not found'.format(node_id))
        for n in self._nodes_table:
            if node_id in n.keys():
                del n[node_id]
        del self._nodes_table[node_id]
        

class GraphAdjacencyMatrix(object):
    def __init__(self, size):
        self._adj_matrix = [[0 for i in range(size)] for i in range(size)]
        self._number_of_nodes = size

    def add_node(self):
        for idx, node_links in enumerate(self._adj_matrix):
            node_links.append(0)
            self._adj_matrix[i] = node_links
        self._number_of_nodes += 1
        new_node_links = [0 for i in range(self._number_of_nodes)]
        self._adj_matrix.append(new_node_links)

    def add_edge_directed(self, source_id, target_id, weight=1):
        if (source_id+1 > self._number_of_nodes) or \
            (target_id+1 > self._number_of_nodes):
            raise GraphException('Nodes source_id or target_id out of bound')
        self._adj_matrix[source_id][target_id] = weight

    def add_edge(self, node_1, node_2, weight=1):
        self.add_edge_directed(node_1, node_2, weight=1)
        self.add_edge_directed(node_2, node_1, weight=1)
