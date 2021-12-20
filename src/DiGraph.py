
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.dict_v=dict()
        self.dict_e=dict(dict())
        self.v_size=0
        self.e_size=0


    def v_size(self) -> int:
        return self.v_size

    def e_size(self) -> int:
        return self.e_size

    def get_all_v(self) -> dict:
        return self.dict_v

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = dict()
        if(id1 not in self.dict_v):
            return ans
        for i in dict_e.keys():
            if id1 in dict_e[i]:
                ans[i] = dict_v[i]
        return ans
    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass
