from src.DiGraph import DiGraph


class SaveJson:
    def __init__(self, g: DiGraph):
        self.Edges = [{}]
        self.Nodes = [{}]
        k = 0
        if g is not None:
            for i in g.Edges.keys():
                for j in g.Edges[i]:
                    if k != 0:
                        self.Edges.insert(k, {})
                    self.Edges[k]["src"] = j
                    self.Edges[k]["w"] = g.Edges[i][j]
                    self.Edges[k]["dest"] = j
                    k += 1
            j = 0
            for i in g.Nodes.keys():
                if j != 0:
                    self.Nodes.insert(j, {})
                self.Nodes[j]["pos"] = g.Nodes[i]
                self.Nodes[j]["id"] = i
                j += 1
