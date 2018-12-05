import unittest

from data_structure.graph import Graph

def get_mock_graph():
	g = Graph()
	for i in range(100):
	    g.add_node(i)
	for i in range(5,100):
	    g.add_edge(i-4,i-3)
	    g.add_edge(i-4,i-2)
	    g.add_edge(i-4,i-1)
	    g.add_edge(i-4,i)
	return g

class TestGraph(unittest.TestCase):
	def test_graph_creation(self):
		get_mock_graph()
