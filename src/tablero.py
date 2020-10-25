class tablero:
    def __init__(self,n):
        self.n = n
        self.modify = False
        self.PlayerArrPos = [] 
        self.createTable()
    def createTable(self):
        self.tablero = [[] for x in range(self.n)]
        number = 0
        for xC in range(self.n):
            for yC in range(self.n):
                self.tablero[xC].append(number)
                number += 1
        cantNodos = self.n * self.n
        self.Matrix = [[] for x in range(cantNodos)]
        for i in range(cantNodos):
            for j in range(cantNodos):
                self.Matrix[i].append(1)

    def statusMod(self, update):
        self.modify = update
        return self.modify

    def viewTable(self):
        b = ""
        agregado = False
        print(self.PlayerArrPos)
        for x in range(self.n):
            for y in range(self.n):
                agregado= False
                for i in self.PlayerArrPos:
                    if x == i[0] and y == i[1]:
                        b += '#' + '\t'
                        agregado = True
                if not agregado:
                    b += str(self.tablero[x][y]) + '\t'

            print(b)
            b = ""

    def setPlayerPosinit(self, Xp, Yp):
        self.PlayerArrPos.append([Xp, Yp])

    def setPlayerPos(self, Xp, Yp, numberPl):
            self.PlayerArrPos[numberPl][0] += Xp
            self.PlayerArrPos[numberPl][1] += Yp

    def setWall(self, Node1,Node2):
        self.Matrix[Node1][Node2] = 0
        self.Matrix[Node2][Node1] = 0
        self.statusMod(True)
