from queue import PriorityQueue
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
    def __init__(self, nodoInx, nodoIny, nodoEndx, nodoEndy):
        self.nIn = (nodoInx, nodoIny)
        self.nEnd = (nodoEndx , nodoEndy)

    def Neighbor(self, mat):
        dx = [1, -1, 0, 0] 
        dy = [0, 0, 1, -1]
        n = len(mat)
        oSet = PriorityQueue() 
        cSet = [False]*(n*n)
        cPath = PriorityQueue() 
        Xg = self.nIn[0]
        Yg = self.nIn[1]
        def valid(i):
            n = len(mat)
            return Xg + dx[i] < n and Yg + dy[i] < n and not cSet[mat[Xg + dx[i]][Yg + dy[i]].NodeNumber]

        oSet.put(mat[Xg][Yg])
        terminado = False
        input()
        while not oSet.empty() and terminado != True:
            Ganador = oSet.get()
            Xg = Ganador.XC
            Yg = Ganador.YC
            print("Nodo: ",Xg, Yg, "F: ",Ganador.fC)
            input()
            cPath.put(Ganador)
            cSet[mat[Xg][Yg].NodeNumber] = True
            for i in range(4):
                    if valid(i):
                        mat[Xg + dx[i]][Yg + dy[i]].SethC(self.nEnd[0], self.nEnd[1], mat[Xg][Yg].gC)
                        if (Xg + dx[i]) == self.nEnd[0] and (Yg + dy[i]) == self.nEnd[1]:
                            terminado = True
                            cPath.put(mat[Xg + dx[i]][Yg + dy[i]])
                            print("Encontrado")
                            break
                        oSet.put(mat[Xg + dx[i]][Yg + dy[i]])
        return cPath

class Casilla(object):
    def __init__(self, xC, yC, nN):
        self.NodeNumber = nN
        self.XC = xC
        self.YC = yC
        self.gC = 0
        self.hC = 0
        self.fC = 0 

    def SethC(self, xO, yO, g):
        self.gC = 1 + g 
        dx = self.XC - xO
        dy = self.YC - yO
        self.hC = abs(dx) + abs(dy) 
        self.fC = self.gC + self.hC

    def __lt__(self, otro):
        return self.fC < otro.fC

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
tabla = tablero(9, 9)
tabla.createTable()
tabla.viewTable()
print("quiero llegar a: 0, 0")
Algoritmo = A_star(2, 1, 0, 2)
Path = Algoritmo.Neighbor(tabla.mat)
cont = 0
while not Path.empty():
    c = Path.get()
    cont += 1
    print(c.NodeNumber)
print("Cantidad:",cont)
