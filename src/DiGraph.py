
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self):
        self.Edges=dict(dict())
        self.Nodes=dict()
        self.v_s=0
        self.e_s=0
        self.mc=0


    def v_size(self) -> int:
        return self.v_s

    def e_size(self) -> int:
        return self.e_s

    def get_all_v(self) -> dict:
        return self.Nodes
        # dict_=dict()
        # for i in self.Nodes.keys():
        #     temp1=self.all_out_edges_of_node(i).__len__()
        #     temp2=self.all_in_edges_of_node(i).__len__()
        #     dict_[i]=str(i)+":|edges out| "+str(temp1)+" |edges in| "+str(temp2)
        # return dict_

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
        if node_id not in self.Nodes:
            return False
        del self.Edges[node_id]
        del self.Nodes[node_id]
        for i in self.Edges.keys():
            if 0 in self.Edges[i]:
                del self.Edges[i][0]
                self.e_s-=1
        self.v_s-=1
        self.mc+=1
        if node_id not in self.Nodes:
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 not in self.Nodes or node_id2 not in
        self.Nodes or node_id2 not in self.Edges[node_id1]):
            return
        del self.Edges[node_id1][node_id2]
        self.e_s -= 1
        self.mc += 1
        if node_id2 not in self.Edges[node_id1]:
            return True
        else:
            return False

    def __repr__(self):
        s="|V|="+str(self.v_s)+" , |E|="+str(self.e_s)
        return s



