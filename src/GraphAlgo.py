import json
import sys

import requests
from typing import List

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Node import Node


def min_val(nodes: dict()) -> int:
    m = sys.maxsize
    temp = -1
    for i in range(len(nodes)):
        if nodes[i].info == "white":
            if nodes[i].weigh < m:
                m = nodes[i].weigh
                temp = nodes[i].id

    if temp == -1:
        for i in range(len(nodes)):
            if nodes[i].info == "white":
                temp = nodes[i].id
                break

    return temp


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph=None):
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
        pass

    # with open(file_name, 'w') as f:
    #     ob = requests.get(file_name).json()
    #     Edge = []
    #
    #     for i in self.graph.dict_e:
    #         for j in self.graph.dict_e[i]:
    #             edge = {"src ": i,
    #                     "w ": self.graph.dict_e[i][j],
    #                     "dest": j}
    #             Edge.append(edge)
    #      ob["Edge"].appae
    #      json.dump("Edge: ", f)
    #      json.dump(Edge, f)
    #      for i in Edge:
    #         json.dump(i, f)

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        nodes = self.path(id1)
        if nodes[id2].weigh == sys.maxsize:
            ans = (float('inf'), [])
        else:
            w = nodes[id2].weigh
            p = []
            p.insert(0, id2)
            j = nodes[id2].tag
            while j != id1:
                p.insert(0, j)
                j = nodes[j].tag
            p.insert(0, id1)
            ans = (w, p)

        return ans

    def path(self, id1: int) -> dict():
        nodes = dict()
        for i in self.graph.dict_v.keys():
            n = Node(i, self.graph.dict_v[i])
            if i in self.graph.dict_e[id1]:
                n.weigh = self.graph.dict_e[id1][i]
            else:
                n.weigh = sys.maxsize
            n.tag = -1
            n.info = "white"
            nodes[i] = n
        nodes[id1].weigh = 0
        nodes[id1].tag = 0
        i = id1
        t = 0
        size = self.get_graph().v_size()
        while t < size:
            if nodes[i].info != "white":
                t += 1
                continue
            nodes[i].info = "black"
            for j in self.graph.dict_e[i].keys():
                temp_j = nodes[j].weigh
                temp_i = nodes[i].weigh
                if temp_i != sys.maxsize:
                    w = self.graph.dict_e[i][j]
                    m = min(temp_j, temp_i + w)
                    nodes[j].weigh = m
                if temp_j != nodes[j].weigh or i == id1:
                    nodes[j].tag = i
            i = min_val(nodes)
            t += 1
        return nodes

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):

        pass

    def plot_graph(self) -> None:
        pass
