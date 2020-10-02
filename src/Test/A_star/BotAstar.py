from Test.A_star.A_star_Man import *
class PlayerAstar:
    def __init__(self, num):
        self.X = 0
        self.Y = 0
        self.wallCount = 0
        self.Astar = A_star()
        self.Path = []
        self.PlayerNum = num 

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
        input("en la pensada")
        print(self.PlayerNum, self.X, self.Y)
        print(self.Path)
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

        if self.Path == []:
            ans = True
        
        print("El path que quedo es")
        b = ""
        for i in self.Path:
            b += str(i.NodeNumber) + ' '
        print(b)
        b = ""
        return ans 

    def setXandSetY(self, X, Y):
        self.X = X
        self.Y = Y

#Player = PlayerAstar()
#Player.setXandSetY(0 , 7)
#tabla = tablero(9, 9)
#tabla.createTable()
#tabla.viewTable()
#muros de ejemplo
# Espacio de prueba
#Algorimo = A_star()
#Algorimo.Search(0 , 0, 8, 4, tabla.mat)

#Player.think(tabla)
