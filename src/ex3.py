import random
import sys
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def get_v(graph: DiGraph, num: int):
    n = graph.v_size()
    my_list = []

    while my_list.__len__() < num:
        rand = int(random.uniform(0, n))
        count = 0
        for i in graph.Nodes.keys():
            if count == rand:
                my_list.append(i)
                break
            count += 1
    return my_list


def algo(file: str):
    graph_algo = GraphAlgo()
    graph_algo.load_from_json(file)
    print(graph_algo.get_graph())
    print(graph_algo.centerPoint())
    list1 = get_v(graph_algo.get_graph(), 2)
    print(graph_algo.shortest_path(list1[0], list1[1]))
    list2 = get_v(graph_algo.get_graph(), 4)
    print(graph_algo.TSP(list2))
    graph_algo.plot_graph()
    graph_algo.save_to_json("ex3.json")


if __name__ == '__main__':

    if len(sys.argv) == 2:
        algo(sys.argv[1])

    else:
        algo("A0.json")
        algo("A1.json")
        algo("A2.json")
        algo("A3.json")
        algo("A4.json")
        algo("A5.json")
        algo("T0.json")


