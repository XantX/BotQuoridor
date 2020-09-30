from queue import PriorityQueue
from Tablero import *
#Pruebas de implementación sin librerías
class A_star:
    def __init__(self):
        self.nIn = (0, 0)
        self.nEnd = (0, 0)

    def Neighbor(self, mat):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(mat)
        oSet = ListaMod() 
        cSet = [False]*(n*n)
        Xg = self.nIn[0]
        Yg = self.nIn[1]
        def valid(i):
            n = len(mat)
            ConditionX = Xg + dx[i] < n and Xg + dx[i] >= 0
            ConditionY = Yg + dy[i] < n and Yg + dy[i] >= 0

            return  ConditionX and ConditionY and not cSet[mat[Xg + dx[i]][Yg + dy[i]].NodeNumber]

        oSet.add(mat[Xg][Yg])
        terminado = False
        while not oSet.emptyS() and terminado != True:
            Ganador = oSet.MayorF()
            Xg = Ganador.XC
            Yg = Ganador.YC
            #print("Primero en salir",mat[Xg][Yg].NodeNumber)
            cSet[mat[Xg][Yg].NodeNumber] = True
            for i in range(4):
                    if valid(i):
                        if oSet.count(mat[Xg + dx[i]][Yg + dy[i]]):
                            #print("Se le califico para update", mat[Xg + dx[i]][Yg + dy[i]])
                            oSet.update(Ganador, mat[Xg + dx[i]][Yg + dy[i]])
                        else:
                            #Se quedo en el enlace de padres
                            mat[Xg + dx[i]][Yg + dy[i]].SethC(self.nEnd[0], self.nEnd[1], Ganador)
                            #print("Hermano Infectado", mat[Xg + dx[i]][Yg + dy[i]].NodeNumber)
                            if (Xg + dx[i]) == self.nEnd[0] and (Yg + dy[i]) == self.nEnd[1]:
                                terminado = True
                                Final = mat[Xg + dx[i]][Yg + dy[i]]
                                print("desde", self.nIn[0], self.nIn[1], "va hacia", self.nEnd[0], self.nEnd[1])
                                print("Encontrado")
                                #print(Final.NodeNumber, Final.gC) 
                                cPath = []  
                                Path = Final.Padre
                                cPath.append(Final)
                                while Path.Padre != None:
                                    #print(Path.NodeNumber, Path.gC)
                                    cPath.append(Path)
                                    Path = Path.Padre
                                return cPath
                            oSet.add(mat[Xg + dx[i]][Yg + dy[i]])

        return False

    def Search(self,nodoInx, nodoIny, nodoEndx, nodoEndy, mat):
        #implementacion de matriz para el calculo de camino valido
        self.nIn = (nodoInx, nodoIny)
        self.nEnd = (nodoEndx , nodoEndy)
        ans = self.Neighbor(mat)
        return ans

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
        menor = self.Arreglo[0]
        cont = 0
        for j in self.Arreglo:
            if menor.fC > j.fC:
                menor = j

        aux = self.Arreglo.pop(self.Arreglo.index(menor))
        self.size -= 1

        return menor

    def update(self, Ganador, objeto):
        for i in self.Arreglo:
            if i.NodeNumber == objeto.NodeNumber:
                if i.gC > Ganador.gC + 1:
                    i.SethCUp(Ganador)
                    break

#tabla = tablero(9, 9)
#tabla.createTable()
#tabla.viewTable()

#print("quiero llegar a: 0, 4")
#Algoritmo = A_star()
#Path = Algoritmo.Search(3, 2,0, 0, tabla.mat) 
