
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.dict_v=dict()
        self.dict_e=dict(dict())
        self.v_size=0
        self.e_size=0
        self.mc=0


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
        for i in self.dict_e.keys():
            if id1 in self.dict_e[i]:
                ans[i] =self.dict_e[i][id1]
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        ans=dict()
        if id1 not in self.dict_v:
            return ans
        for i in self.dict_e[id1]:
            ans[i]=self.dict_e[id1][i]
        return ans


    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if( id1 not in self.dict_v or id2 not in
        self.dict_v or weight<0 or id2 in self.dict_e[id1]):
            return
        self.dict_e[id1][id2]=weight
        self.e_size+=1
        self.mc+=1
        if id2 in self.dict_e[id1]:
            return True
        else:
            return False


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.dict_v:
            return
        #n=Node (node_id,pos[0],pos[1])
        self.dict_v[node_id]=pos
        self.dict_e[node_id]={}
        self.mc+=1
        self.v_size+=1
        if node_id in self.dict_v:
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
        if node_id not in self.dict_v and node_id not in self.dict_v:
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 not in self.dict_v or node_id2 not in
        self.dict_v or node_id2 in self.dict_e[node_id1]):
            return
        del self.dict_e[node_id1][node_id2]
        self.e_size -= 1
        self.mc += 1
        if node_id2 not in self.dict_e[node_id1]:
            return True
        else:
            return False
