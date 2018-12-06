import unittest

from data_structure.graph import Graph
from data_structure.basic import Queue
from data_structure.tree import PriorityQueue

from algorithm.graph import breath_first_search, dijkstra_search

def get_mock_graph():
    g = Graph()
    for i in range(100):
        g.add_node(i)
    for i in range(5,100):
        g.add_edge(i-5,i-4)
        g.add_edge(i-5,i-3)
        g.add_edge(i-5,i-2)
        g.add_edge(i-5,i-1)
        g.add_edge(i-5,i)
    return g

def get_queue():
    return Queue()

def get_priority_queue():
    return PriorityQueue()

class TestGraph(unittest.TestCase):
    def test_graph_creation(self):
        get_mock_graph()

    def test_graph_bfs(self):
        g = get_mock_graph()
        q = get_queue()
        node_start_id = 25
        node_goal_id = 75
        breath_first_search(g, q, node_start_id, node_goal_id)

    def test_graph_dijkstra(self):
        g = get_mock_graph()
        q = get_priority_queue()
        node_start_id = 25
        node_goal_id = 75
        dijkstra_search(g, q, node_start_id, node_goal_id)
