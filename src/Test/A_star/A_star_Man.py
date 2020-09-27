#from Queue import PriorityQueue
#Pruebas de implementación sin librerías
GConect =[[0, 1, 0, 1],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [1, 0, 1, 0]]

GDic = [[1, 3],
        [0, 2],
        [1, 3],
        [0, 2]]

class A_star:
    def __init__(self, nodoIn, nodoEnd):
        self.nIn = nodoIn
        self.nEnd = nodoEnd

class Casilla:
    def __init__(self, xC, yC, nN):
        self.NodeNumber = nN
        self.XC = xC
        self.YC = yC
        self.gC = 0
        self.hC = 0
        self.fC = 0 

    def SetgC(self, GC):
        self.gC = GC

    def SethC(self, xO, yO):
        dx = self.XC - xO
        dy = self.YC - yO
        self.hC = abs(dx) + abs(dy) 
    def F(self):
        self.fC = self.gC + self.hC
        return self.fC

class tablero:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def createTable(self):
        self.mat = [[] for x in range(self.x)]
        number = 0
        for xC in range(self.x):
            for yC in range(self.y):
                self.mat[xC].append(Casilla(xC, yC, number))
                number = number + 1

    def viewTable(self):
        b = ""
        for x in range(self.x):
            for y in range(self.y):
                b += str(self.mat[x][y].NodeNumber) + '\t'
            print(b)
            b = ""
tabla = tablero(4, 4)
tabla.createTable()
tabla.viewTable()

