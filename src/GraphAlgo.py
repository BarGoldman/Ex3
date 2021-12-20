import json
import requests
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        with open(file_name, "r") as fp:
            di = json.load(fp)
            for k in di["Nodes"]:
                i = k["id"]
                pos = k["pos"]
                g.add_node(i, pos)
            for k in di["Edges"]:
                src = k["src"]
                dest = k["dest"]
                w = k["w"]
                g.add_edge(src, dest, w)
        self.__init__(g)

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w') as f:
            ob = requests.get(file_name).json()
            Edge = []

            for i in self.graph.dict_e:
                for j in self.graph.dict_e[i]:
                    edge = {"src ": i,
                            "w ": self.graph.dict_e[i][j],
                            "dest": j}
                    Edge.append(edge)
            ob["Edge"].appae
            json.dump("Edge: ", f)
            json.dump(Edge, f)
            for i in Edge:
                json.dump(i, f)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
