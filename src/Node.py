class Node:
    def __init__(self, i, pos: tuple):
        self.id = i
        self.weigh = 0
        self.tag = 0
        self.info = ""
        if pos is not None:
            self.x = float(pos[0])
            self.y = float(pos[1])
            self.z = float(pos[2])
        self.edges_out = 0
        self.edges_in = 0


