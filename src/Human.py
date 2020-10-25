from Player.Player import *
from tablero import * 
class Human(Player):
    def move(self, Tablero):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = self.xTb 
        def valid(i):
            ConditionX = self.X + dx[i] < n and self.X + dx[i] >= 0
            ConditionY = self.Y + dy[i] < n and self.Y + dy[i] >= 0

            if (ConditionX and ConditionY):
                N1 = Tablero.tablero[self.X][self.Y]
                N2 = Tablero.tablero[self.X + dx[i]][self.Y + dy[i]]
                if Tablero.Matrix[N1][N2]:
                    return True
                else:
                    return False

            return False 
        
        print("estoy en la casilla", self.X, self.Y)
        print("up , right, down, left")
        validOpcion = False
        while not validOpcion:
            opcion = input("eliga una opcion --->")
            if opcion.lower() == "up":
                if valid(0):
                    self.X += dx[0]
                    self.Y += dy[0]
                    return dx[0], dy[0]
                    validOpcion = True
                else:
                    print("no se puede ir ahi")
            elif opcion.lower() == "right":
                if valid(1):
                    self.X += dx[1]
                    self.Y += dy[1]
                    return dx[1], dy[1]
                    validOpcion = True
                else:
                    print("no se puede ir ahi")
            elif opcion.lower() == "down":
                if valid(2):
                    self.X += dx[2]
                    self.Y += dy[2]
                    return dx[2], dy[2]
                    validOpcion = True
                else:
                    print("no se puede ir ahi")
            elif opcion.lower() == "left":
                if valid(3):
                    self.X += dx[3]
                    self.Y += dy[3]
                    return dx[3], dy[3]
                    validOpcion = True
                else:
                    print("no se puede ir ahi")

    def setMuros(self, Tablero):
        a, b = input("un muro entre los numeros de casilla N N :").split()
        a = int(a)
        b = int(b)
        n = len(Tablero.tablero)
        def valido():
            if a < n*n and a >= 0 and b < n*n and b >= 0:
                return True
            else:
                return False
        while not valido():
            print("el par no es valido")
            a, b = input("un muro entre los numeros de casilla N N :").split()
            a = int(a)
            b = int(b)
        Tablero.setWall(a, b)
# por factorizar
    def think(self, tablero):
        print("elige una opcion")
        print("1) mover")
        print("2) muro")
        print(self.NodeObjetive)
        opcion = input("--->")
        while int(opcion) < 1 or int(opcion) > 2:
            print("opcion invalida")
            print("1) mover")
            print("2) muro")
            opcion = input("--->")

        if opcion == "1":
            ans  = self.move(tablero)
            if self.Win():
                return ans, True
            else:
                return ans, False
        if opcion == "2":
            print("muro")
            self.setMuros(tablero)
            ans = (0, 0)
            
            return ans,False  

# n = 3
# Humano = Human(1,n) 
# Humano.setXandSetY(0, 1)
# tab = tablero(3)
# tab.viewTable()
# Humano.think(tab)
