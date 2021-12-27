from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestBigGraph(TestCase):
    file = "100000.json"
    g = DiGraph()
    g_algo = GraphAlgo(g)
    g_algo.load_from_json(file)

    def test_get_graph(self):
        self.g_algo.get_graph()

    def test_load_from_json(self):
        self.g_algo.load_from_json(self.file)

    def test_save_to_json(self):
        self.g_algo.save_to_json("test")

    def test_shortest_path(self):
        self.g_algo.shortest_path(230, 420)

    def test_tsp(self):
        self.g_algo.TSP([1, 2, 4])

    def test_is_connected(self):
        self.g_algo.is_connected()

    def test_center_point(self):
        self.g_algo.centerPoint()

    def test_plot_graph(self):
        self.g_algo.plot_graph()
