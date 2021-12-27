import random
import sys
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


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
    print(file)
    print(graph_algo.get_graph())
    print("center=", graph_algo.centerPoint())
    list1 = get_v(graph_algo.get_graph(), 2)
    print("node1=", list1[0], ",", "node2=", list1[1], ",", "shortest path=",
          graph_algo.shortest_path(list1[0], list1[1]))
    list2 = get_v(graph_algo.get_graph(), 4)
    print("list:", list2, end='')
    print(",", "TSP=", graph_algo.TSP(list2))
    graph_algo.plot_graph()
    graph_algo.save_to_json("ex3.json")


if __name__ == '__main__':

    if len(sys.argv) == 2:
        algo(sys.argv[1])

    else:
        algo("A0.json")
        print("----------------------")
        algo("A1.json")
        print("----------------------")
        algo("A2.json")
        print("----------------------")
        algo("A3.json")
        print("----------------------")
        algo("A4.json")
        print("----------------------")
        algo("A5.json")
        print("----------------------")
        algo("T0.json")
        print("----------------------")
