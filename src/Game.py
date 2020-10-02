#from Test.A_star.Tablero import * 
from Test.A_star.BotAstar import *
from collections import deque
class Game:
    def __init__(self, X, Y, CantJugadores):
        self.Cant = CantJugadores
        self.Players = deque()
        self.Winner = False
        self.TABLERO = tablero(X, Y)

    def CreatePlayers(self):
        for i in range(self.Cant):
            self.Players.append(PlayerAstar(i))
        self.SetPosition()
        
    def SetPosition(self):
        self.Players[0].setXandSetY(0, 4)
        self.TABLERO.setPlayerPosinit(0 , 4)
        self.Players[1].setXandSetY(8, 4)
        self.TABLERO.setPlayerPosinit(8, 4)

    def Turno(self, Players):
        movement = Players.think(self.TABLERO)
        print("movement", movement)
        if movement == True:
            self.Winner = True
        else:
            print("estaba en")
            print(Players.X, Players.Y)
            self.TABLERO.setPlayerPos(movement[0],movement[1],Players.PlayerNum)

    def main(self):
        self.CreatePlayers()
        self.TABLERO.createTable()
        self.TABLERO.viewTable()
        while not self.Winner:
            print(self.Winner)
            input("Se paro antes de sacar player")
            Player = self.Players[1]
            self.Players.popleft()
            self.Turno(Player)
            self.Players.append(Player)
            input("se para luego de turno")
        print("Ya gano")
Juego = Game(9, 9, 2)
Juego.main()
