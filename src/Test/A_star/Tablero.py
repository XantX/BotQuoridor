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
        self.modify = False
        self.PlayerArrPos = []

    def createTable(self):
        self.mat = [[] for x in range(self.x)]
        number = 0
        for xC in range(self.x):
            for yC in range(self.y):
                self.mat[xC].append(Casilla(xC, yC, number))
                number = number + 1

        self.Matrix = [[] for x in range(self.x * self.y)]
        for i in range(self.x * self.y):
            for j in range(self.x * self.y):
                self.Matrix[i].append(1)

    def Cruce(self, NodeNum1, NodeNum2):
        if self.Matrix[NodeNum1][NodeNum2] == 1:
            return True
        return False
    def setPlayerPosinit(self, Xp, Yp):
        self.PlayerArrPos.append([Xp, Yp])

    def setPlayerPos(self, Xp, Yp, numberPl):
            self.PlayerArrPos[numberPl][0] += Xp
            self.PlayerArrPos[numberPl][1] += Yp

    def setWall(self, Node1,Node2):
        self.Matrix[Node1][Node2] = 0
        self.Matrix[Node2][Node1] = 0
        self.statusMod(True)


    def statusMod(self, update):
        self.modify = update
        return self.modify
    def RestartTable(self):
        for i in range(self.x):
            for j in range(self.y):
                self.mat[i][j].Padre = None
                self.mat[i][j].gC = 0
        
    def viewTable(self):
        b = ""
        for x in range(self.x):
            for y in range(self.y):
                b += str(self.mat[x][y].NodeNumber) + '\t'
            print(b)
            b = ""

#Table = tablero(4, 4)
#Table.createTable()
#Table.viewTable()
#print(Table.Cruce(11,15))
