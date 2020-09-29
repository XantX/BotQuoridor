from A_star_Man import *
from Tablero import *
class PlayerAstar:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.wallCount = 0
        self.Astar = A_star()
    def SearchObjectives(self):
        if self.X == 0 and self.Y == 4:
            Objetives = [(8, y)for y in range(9)]
        elif self.X == 8 and self.Y == 4:
            Objetives = [(0, y)for y in range(9)]
        elif self.X == 4 and self.Y == 0:
            Objetives = [(x, 8)for x in range(9)]
        elif self.X == 4 and self.Y == 8:
            Objetives = [(x, 0)for x in range(9)]
        return Objetives

    def PathResult(self, mat):
        NodeObjetive = self.SearchObjectives()
        Paths = []
        for obj in NodeObjetive:
            Paths.append(self.Astar.Search(self.X, self.Y, obj[0], obj[1], mat) )
        return Paths

    def think(self, mat):
        #Busca su camino
        Paths = self.PathResult(mat)
        print(Paths)
        #Le calcula el camino al enemigo    
        #Elige

    def setXandSetY(self, X, Y):
        self.X = X
        self.Y = Y

Player = PlayerAstar()
Player.setXandSetY(0 , 4)
objetivo = Player.SearchObjectives()
print(objetivo)
tabla = tablero(9, 9)
tabla.createTable()
tabla.viewTable()
# Espacio de prueba
#Algorimo = A_star()
#Algorimo.Search(0 , 0, 8, 4, tabla.mat)
Player.think(tabla.mat)
