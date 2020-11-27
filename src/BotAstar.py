# from Player.Player import *
from src.Player.Player import *
from src.Algoritmos.Astar.A_star import * 
class BotAstar(Player):
    def PathResult(self, Tablero, X , Y ):
        self.Astar = A_star(self.xTb)
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
        print("Tablero se modifico:",tablero.modify)
        if   self.Path == [] or tablero.modify :
            #print(self.PlayerNum, self.X, self.Y)
            self.Path = self.PathResult(tablero.Matrix, self.X, self.Y)
            self.Path.reverse()
        print("El path ganador es")
        b = ""
        for i in self.Path:
            b += str(i.NodeNumber) + ' '
        print(b)
        b = ""
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
# n = 3
# nodos = n*n
# g = [[]for i in range(nodos)]
# for x in range(nodos):
   # for y in range(nodos):
       # g[x].append(1)

# bot = BotAstar(1,n)
# bot.setXandSetY(0,1)
# bot.think(g)
