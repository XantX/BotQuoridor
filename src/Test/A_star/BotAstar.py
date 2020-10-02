from Test.A_star.A_star_Man import *
#from A_star_Man import *
class PlayerAstar:
    def __init__(self, num, xTb, yTb):
        self.X = 0
        self.Y = 0
        self.wallCount = 0
        self.Astar = A_star()
        self.Path = []
        self.PlayerNum = num 
        self.xTb = xTb
        self.yTb = yTb
        self.NodeObjetive = []
    def SearchObjectives(self, Xp, Yp):
        if Xp == 0 and (Yp >= 0 and Yp < self.yTb):
            Objetives = [(self.xTb - 1, y)for y in range(self.yTb)]

        elif Xp == self.xTb - 1 and (Yp >= 0 and Yp < self.yTb):
            Objetives = [(0, y)for y in range(self.yTb)]

        elif  (Xp >= 0 and Xp < self.xTb)and Yp == 0:
            Objetives = [(x, self.ytb - 1)for x in range(self.xTb)]

        elif (Xp >= 0 and Xp < self.xTb) and Yp == self.yTb - 1:
            Objetives = [(x, 0)for x in range(self.xTb)]

        return Objetives

    def PathResult(self, Tablero, X , Y ):
        if self.NodeObjetive == []:
            self.NodeObjetive = self.SearchObjectives(X , Y)
        print(self.NodeObjetive)
        Paths = []
        for obj in self.NodeObjetive:
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
            #print(self.PlayerNum, self.X, self.Y)
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
            return ans, True
        
        print("El path que quedo es")
        b = ""
        for i in self.Path:
            b += str(i.NodeNumber) + ' '
        print(b)
        b = ""
        return ans, False

    def setXandSetY(self, X, Y):
        self.X = X
        self.Y = Y

#tabla = tablero(9, 9)
#tabla.createTable()
#tabla.viewTable()
#Player = PlayerAstar(1, 9, 9)
#Player.setXandSetY(0 , 4)
#Player2 = PlayerAstar(2, 9, 9)
#Player2.setXandSetY(8, 4)
#muros de ejemplo
# Espacio de prueba
#Algorimo = A_star()
#Algorimo.Search(0 , 0, 8, 4, tabla.mat)
#Player.think(tabla)
#tabla.RestartTable()
#Player2.think(tabla)
