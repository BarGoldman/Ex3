class Node:
    def __init__(self, i, pos: tuple):
        self.id = i
        self.weigh = 0
        self.tag = 0
        self.info = ""
        if pos is not None:
            self.x = pos[0]
            self.y = pos[1]
            self.z = pos[2]
