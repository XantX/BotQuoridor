from A_star_Man import *
from Tablero import *
class PlayerAstar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.wallCount = 0
        self.Astar = A_star()
        self.Path = []

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

    def PathResult(self, Tablero, X , Y ):
        NodeObjetive = self.SearchObjectives(X , Y)
        print(NodeObjetive)
        Paths = []
        for obj in NodeObjetive:
            result = self.Astar.Search(X, Y, obj[0], obj[1], Tablero)
            if result != False:
                Paths.append(result)

        PathRes = Paths[0]
        for i in Paths:
            if len(i) < len(PathRes):
                PathRes = i

        return PathRes

    def move(self, casillaObj):
        x = -1 * (self.X - casillaObj.XC) 
        y = -1 * (self.Y - casillaObj.YC)
        self.X += x
        self.Y += y
        return x, y

    def think(self, tablero):
        #Busca su camino
        #verificar si la tabla fue modificada en el turno anterior
        if self.Path == [] or tablero.modify:
            self.Path = self.PathResult(tablero, self.X, self.Y)
            self.Path.reverse()

        print("El path ganador es")
        b = ""
        for i in self.Path:
            b += str(i.NodeNumber) + ' '
        print(b)
        b = ""
        #Le calcula el camino al enemigo    
        #esta parte es para el calculo de los muros 

        #Elige
        ans = self.move(self.Path[0])
        self.Path.pop(0)
        return ans 

    def setXandSetY(self, X, Y):
        self.X = X
        self.Y = Y

Player = PlayerAstar()
Player.setXandSetY(0 , 7)
tabla = tablero(9, 9)
tabla.createTable()
tabla.viewTable()
#muros de ejemplo
tabla.setWall(34, 43) 
tabla.setWall(33, 42) 
tabla.setWall(39, 40) 
tabla.setWall(73, 74) 
tabla.setWall(72, 63)
tabla.setWall(73, 64)
tabla.setWall(80, 71)
tabla.setWall(79, 70)
tabla.setWall(76, 67)
tabla.setWall(79, 78)
# Espacio de prueba
#Algorimo = A_star()
#Algorimo.Search(0 , 0, 8, 4, tabla.mat)

Player.think(tabla)
