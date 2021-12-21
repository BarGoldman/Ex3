
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.Edges=dict()
        self.Nodes=dict(dict())
        self.v_s=0
        self.e_s=0
        self.mc=0

    def di(self):
        return self.__dict__

    def v_size(self) -> int:
        return self.v_s

    def e_size(self) -> int:
        return self.e_s

    def get_all_v(self) -> dict:
        return self.Edges

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans = dict()
        if(id1 not in self.Edges):
            return ans
        for i in self.Edges.keys():
            if id1 in self.Edges[i]:
                ans[i] =self.Edges[i][id1]
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        ans=dict()
        if id1 not in self.Nodes:
            return ans
        for i in self.Edges[id1]:
            ans[i]=self.Edges[id1][i]
        return ans


    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if( id1 not in self.Nodes or id2 not in
        self.Nodes or weight<0 or id2 in self.Edges[id1]):
            return
        self.Edges[id1][id2]=weight
        self.e_s+=1
        self.mc+=1
        if id2 in self.Edges[id1]:
            return True
        else:
            return False


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.Nodes:
            return
        self.Nodes[node_id]=pos
        self.Edges[node_id]={}
        self.mc+=1
        self.v_s+=1
        if node_id in self.Nodes:
            return True
        else:
            return False


    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.dict_v:
            return
        del self.dict_e[node_id]
        del self.dict_v[node_id]
        for i in self.dict_e.keys():
            if 0 in self.dict_e[i]:
                del self.dict_e[i][0]
                self.e_size-=1
        self.v_size-=1
        self.mc+=1
        if node_id not in self.Nodes:
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 not in self.Nodes or node_id2 not in
        self.Nodes or node_id2 in self.Edges[node_id1]):
            return
        del self.dict_e[node_id1][node_id2]
        self.e_size -= 1
        self.mc += 1
        if node_id2 not in self.Edges[node_id1]:
            return True
        else:
            return False

