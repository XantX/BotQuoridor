#from Test.A_star.Tablero import * 
from Test.A_star.BotAstar import *
from collections import deque
from PlayerHuman import *
import time 
import os 
import platform
class Game:
    def __init__(self, X, Y, CantJugadores):
        self.Cant = CantJugadores
        self.Players = deque()
        self.Winner = False
        self.TABLERO = tablero(X, Y)
    def ClearPantalla(self):
        time.sleep(1)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def CreatePlayers(self):
        #for i in range(self.Cant):
        #self.Players.append(PlayerAstar(i, self.TABLERO.x, self.TABLERO.y))
        self.Players.append(PlayerAstar(0, self.TABLERO.x, self.TABLERO.y))
        self.Players.append(Human(1, self.TABLERO.x, self.TABLERO.y))
        self.SetPosition()
        
    def SetPosition(self):
        self.Players[0].setXandSetY(0, 4)
        self.TABLERO.setPlayerPosinit(0 , 4)
        self.Players[1].setXandSetY(8, 4)
        self.TABLERO.setPlayerPosinit(8, 4)

    def Turno(self, Players):
        movement = Players.think(self.TABLERO)
        self.TABLERO.RestartTable()
        print("movement", movement)
        if movement[1] == True:
            self.Winner = True
            self.TABLERO.setPlayerPos(movement[0][0],movement[0][1],Players.PlayerNum)
        else:
            #print("estaba en")
            #print(Players.X, Players.Y)
            self.TABLERO.setPlayerPos(movement[0][0],movement[0][1],Players.PlayerNum)

    def main(self):
        self.CreatePlayers()
        self.TABLERO.createTable()
        while not self.Winner:
            self.ClearPantalla()
            self.TABLERO.viewTable()
            print("Winner?:",self.Winner)
            Player = self.Players[0]
            self.Players.popleft()
            print("turno de el jugador", Player.PlayerNum)
            self.Turno(Player)
            self.Players.append(Player)
        self.TABLERO.viewTable()
        print("Ya gano")
Juego = Game(9, 9, 2)
Juego.main()
