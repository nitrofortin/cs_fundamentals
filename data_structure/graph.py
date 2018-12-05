class GraphException(Exception):
    pass

class GraphNode(object):
    def __init__(self, value=None):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, node, weight=1):
        self.neighbors[node] = weight

    def get_degree(self):
        return sum(self.neighbors.values())

    def get_neighbors(self):
        return list(self.neighbors.keys())

    def __contains__(self, node_value):
        return (node_value in self.neighbors.keys())



class NullNode(GraphNode):
    def __init__(self, value=None):
        self.value = None
    

class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.number_of_nodes = 0
        self._recovering_state = self

    def add_node(self, node_value):
        n = GraphNode(node_value)
        if node_value in self.nodes.keys():
            print('Node {} already exists'.format(node_value))
        else:
            self.number_of_nodes += 1
            self.nodes[node_value] = n
        
    def add_edge(self, source, origin, weight=1):
        if source not in self.nodes.keys() or origin not in self.nodes.keys():
            raise GraphException('Node not in graph nodes')
        node_source = self.nodes[source]
        node_origin = self.nodes[origin]
        node_source.add_neighbor(origin, weight)
        node_origin.add_neighbor(source, weight)

    def add_directed_edge(self, source, origin, weight=1):
        if source not in self.nodes.keys() or origin not in self.nodes.keys():
            raise GraphException('Node not in graph nodes')
        node_source = self.nodes[source]
        node_source.add_neighbor(origin, weight)

    def get_node(self, node_value):
        for n in self.nodes:
            if n.value == node_value:
                return n
        return NullNode()

    def delete_node(self, node_value):
        for n in self.nodes:
            if node_value in n:
                del n.neighbors[node_value]
        del self.nodes[node_value]

    def __contains__(self, node):
        for n in self.nodes:
            if n == node:
                return True
        return False

    def __iter__(self):
        return iter(self.nodes.values())


