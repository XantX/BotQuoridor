from queue import PriorityQueue
class Casilla(object):
    def __init__(self, xC, yC, nN):
        self.NodeNumber = nN
        self.XC = xC
        self.YC = yC
        self.gC = 0
        self.hC = 0
        self.fC = 0 
        self.Padre = None

    def SethC(self, xO, yO, casilla):
        self.gC = 1 + casilla.gC 
        self.Padre = casilla
        dx = self.XC - xO
        dy = self.YC - yO
        self.hC = abs(dx) + abs(dy) 
        self.fC = self.gC + self.hC

    def SethCUp(self, Ganador):
        self.gC = 1 + Ganador.gC 
        self.fC = self.gC + self.hC
        self.Padre = Ganador 

    def __lt__(self, otro):
        return self.gC < otro.gC
###
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

