import StackX
class Graph:

    SIZE=20

    def __init__(self):
        self.vertexList=[0]*self.SIZE
        self.adjMat=[0][0]*self.SIZE
        self.stackX=StackX.StackX
        