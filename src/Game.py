from tablero import *
from Human import *
from BotAstar import *
from collections import deque
import time 
import os 
import platform
class Game:
    def __init__(self, X, CantJugadores):
        self.Cant = CantJugadores
        self.Players = deque()
        self.Winner = False
        self.TABLERO = tablero(X)

    def ClearPantalla(self):
        time.sleep(1)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def CreateBots(self): 

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
        print("Ya gano", Player.PlayerNum)

