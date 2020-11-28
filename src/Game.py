from src.tablero import *

from src.Human import *
from src.BotAstar import *

from collections import deque
#import pygame as pg
import time 
import os 
import platform
class Game:
    def __init__(self, X, CantJugadores):
        self.Cant = CantJugadores
        self.Players = deque()
        self.Winner = False
        ## Crea tablero
        self.TABLERO = tablero(X)
        ## Crea jugador humano y bot
        self.Human = Human(0,X)
        self.Bot = BotAstar(1,X)
        self.Human.setXandSetY(0,4)
        self.Bot.setXandSetY(8,4)
        ### Insertar a los jugador en el tablero 
        self.Players.append(self.Human)
        self.Players.append(self.Bot)
        ### Le da sus posiciones iniciales
        self.TABLERO.setPlayerPosinit(0,4)
        self.TABLERO.setPlayerPosinit(8,4)

    def ClearPantalla(self):
        time.sleep(1)
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def Turno(self, Players):
        movement = Players.think(self.TABLERO)
        print("movement", movement)
        if movement[1] == True:
            self.Winner = True
            self.TABLERO.setPlayerPos(movement[0][0],movement[0][1],Players.PlayerNum)
        else:
            self.TABLERO.setPlayerPos(movement[0][0],movement[0][1],Players.PlayerNum)

    def caracter_game(self):
        while not self.Winner:
            self.ClearPantalla()
            self.TABLERO.viewTable()
            Player = self.Players[0]
            self.Players.popleft()
            print("Turno de:", '#' if Player.PlayerNum == 0 else '$')
            self.Turno(Player)
            self.Players.append(Player)
        self.TABLERO.viewTable()
        print("Winner Player:", Player.PlayerNum)
    
    def main(self):
        self.caracter_game()
        



