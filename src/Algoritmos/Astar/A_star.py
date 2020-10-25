from Algoritmos.Astar.Tablero import *
# from Tablero import *
class A_star:
    def __init__(self, n):
        self.nIn = (0, 0)
        self.nEnd = (0, 0)
        self.tableroobj = tabla(n)
        self.tablero = self.tableroobj.tablero
        self.n = n

    def sol(self, matrix):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        oSet = ListaMod()
        cSet = [False]*(self.n*self.n)
        Xg = self.nIn[0]
        Yg = self.nIn[1]
        def valid(i):
            ConditionX = Xg + dx[i] < self.n and Xg + dx[i] >= 0
            ConditionY = Yg + dy[i] < self.n and Yg + dy[i] >= 0
            if not (ConditionX and ConditionY):
                return False
            elif cSet[self.tablero[Xg + dx[i]][Yg + dy[i]].NodeNumber]:
                return False
            elif not matrix[Ganador.NodeNumber][self.tablero[Xg + dx[i]][Yg + dy[i]].NodeNumber]:
                return False
            return True

        init = self.tablero[Xg][Yg]
        oSet.add(init)
        terminado = False
        while not oSet.emptyS() and terminado != True:
            Ganador = oSet.MayorF()
            Xg = Ganador.XC
            Yg = Ganador.YC
            cSet[Ganador.NodeNumber] = True
            for i in range(4):
                if valid(i):
                    if oSet.count(self.tablero[Xg + dx[i]][Yg + dy[i]]):
                        oSet.update(Ganador, self.tablero[Xg + dx[i]][Yg + dy[i]])
                    else:
                        neighbour = self.tablero[Xg + dx[i]][Yg + dy[i]]
                        neighbour.SethC(self.nEnd[0], self.nEnd[1],Ganador)
                        if (Xg + dx[i]) == self.nEnd[0] and (Yg + dy[i]) == self.nEnd[1]:
                            terminado = True
                            Final = neighbour 
                            cPath = []
                            Path = Final.Padre
                            cPath.append(Final)
                            while Path.Padre != None:
                                cPath.append(Path)
                                Path = Path.Padre
                            return cPath
                        oSet.add(neighbour)
        return False

    def Search(self,Inx, Iny, Endx, Endy,matrix):
        self.nIn = (Inx, Iny)
        self.nEnd = (Endx, Endy)
        ans = self.sol(matrix) 
        self.tablero.RestartTable()
        print("todo correcto")
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
# print("Recivido")
# g = [[]for i in range(81)]
# for x in range(81):
   # for y in range(81):
       # g[x].append(1)
# algo = A_star(9)
# algo.Search(0, 4, 8, 4, g)
