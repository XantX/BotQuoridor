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
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(mat)
        oSet = ListaMod() 
        cSet = [False]*(n*n)
        cPath = PriorityQueue() 
        Xg = self.nIn[0]
        Yg = self.nIn[1]
        def valid(i):
            n = len(mat)
            return Xg + dx[i] < n and Yg + dy[i] < n and not cSet[mat[Xg + dx[i]][Yg + dy[i]].NodeNumber]

        oSet.add(mat[Xg][Yg])
        terminado = False
        while not oSet.emptyS() and terminado != True:
            Ganador = oSet.MayorF()
            Xg = Ganador.XC
            Yg = Ganador.YC
            print("Nodo: ",Xg, Yg, "F: ",Ganador.fC)
            input()
            cSet[mat[Xg][Yg].NodeNumber] = True
            for i in range(4):
                    if valid(i):
                        if oSet.count(mat[Xg + dx[i]][Yg + dy[i]]):
                            oSet.update(Ganador, mat[Xg + dx[i]][Yg + dy[i]])
                        else:
                            #Se quedo en el enlace de padres
                            mat[Xg + dx[i]][Yg + dy[i]].SethC(self.nEnd[0], self.nEnd[1], Ganador)
                            if (Xg + dx[i]) == self.nEnd[0] and (Yg + dy[i]) == self.nEnd[1]:
                                terminado = True
                                Final = mat[Xg + dx[i]][Yg + dy[i]]
                                print("Encontrado")
                                break
                            oSet.add(mat[Xg + dx[i]][Yg + dy[i]])
        print(Final.NodeNumber, Final.gC) 
        Path = Final.Padre
        cPath.put(Final)
        while Path.Padre != None:
            print(Path.NodeNumber, Path.gC)
            Path = Path.Padre
            cPath.put(Path)

        return cPath
class ListaMod:
    def __init__(self):
        self.Arreglo = []
        self.size = 0

    def emptyS(self):
        if self.size == 0:
            return True
        else:
            return False

    def add(self, objeto):
        self.Arreglo.append(objeto)
        self.size += 1

    def count(self, objeto):
        for i in self.Arreglo:
            if(i.NodeNumber == objeto.NodeNumber):
                return True
        return False

    def MayorF(self):
        #error
        menor = self.Arreglo[0]
        cont = 0
        for j in self.Arreglo:
            print("indice:", j.NodeNumber, j.fC)
            if menor.fC > j.fC:
                menor = j

        aux = self.Arreglo.pop(self.Arreglo.index(menor))
        print("salio de OS: ", aux.NodeNumber)
        self.size -= 1

        return menor

    def update(self, Ganador, objeto):
        for i in self.Arreglo:
            if i.NodeNumber == objeto.NodeNumber:
                if i.gC > Ganador.gC + 1:
                    i.SethCUp(Ganador)
                    break

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
print("quiero llegar a: 0, 2")
Algoritmo = A_star(8, 4, 0, 4)
Path = Algoritmo.Neighbor(tabla.mat)
