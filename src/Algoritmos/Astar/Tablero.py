class tabla():
    def __init__(self, h):
        self.h = h
        self.tablero = [[] for i in range(h)]
        self.createTable()

    def RestartTable(self):
        for i in range(self.h):
            for j in range(self.h):
                self.tablero[i][j].Padre = None
                self.tablero[i][j].gC = 0

    def createTable(self):
        number = 0
        for xC in range(self.h):
            for yC in range(self.h):
                self.tablero[xC].append(Casilla(xC,yC,number))
                number += 1
        b = ""

        for x in range(self.h):
            for y in range(self.h):
                b += str(self.tablero[x][y].NodeNumber) + '\t'
            print(b)
            b = ""

class Casilla():
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
