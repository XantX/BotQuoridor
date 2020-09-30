from A_star_Man import *
from Tablero import *
class PlayerAstar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.wallCount = 0
        self.Astar = A_star()

    def SearchObjectives(self, Xp, Yp):
        if Xp == 0 and (Yp >= 0 and Yp < 9):
            Objetives = [(8, y)for y in range(9)]

        elif Xp == 8 and (Yp >= 0 and Yp < 9):
            Objetives = [(0, y)for y in range(9)]

        elif  (Xp >= 0 and Xp < 9)and Yp == 0:
            Objetives = [(x, 8)for x in range(9)]

        elif (Xp >= 0 and Xp < 9) and Yp == 8:
            Objetives = [(x, 0)for x in range(9)]

        return Objetives

    def PathResult(self, mat):
        NodeObjetive = self.SearchObjectives(self.X , self.Y)
        print(NodeObjetive)
        Paths = []
        for obj in NodeObjetive:
            result = self.Astar.Search(self.X, self.Y, obj[0], obj[1], mat)
            if result != False:
                Paths.append(result)

        PathRes = Paths[0]
        for i in Paths:
            if len(i) < len(PathRes):
                PathRes = i

        return PathRes

    def think(self, tablero):
        #Busca su camino
        Path = self.PathResult(tablero.mat)

        print("El path ganador es")
        b = ""
        for i in Path:
            b += str(i.NodeNumber) + ' '
        print(b)
        b = ""
        #Le calcula el camino al enemigo    

        #Elige

    def setXandSetY(self, X, Y):
        self.X = X
        self.Y = Y

Player = PlayerAstar()
Player.setXandSetY(0 , 7)
tabla = tablero(9, 9)
tabla.createTable()
tabla.viewTable()
# Espacio de prueba
#Algorimo = A_star()
#Algorimo.Search(0 , 0, 8, 4, tabla.mat)
Player.think(tabla)
