from Test.A_star.Tablero import * 
class Human:
    def __init__(self, num, xTb, yTb):
        self.PlayerNum = num
        self.X = 0 
        self.Y = 0
        self.xTb = xTb
        self.yTb = yTb
        self.NodeObjetive = []
    def setXandSetY(self, x, y):
        self.X = x
        self.Y = y
        self.NodeObjetive = self.SearchObjectives(self.X, self.Y)

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

    def Win(self):
        for i in self.NodeObjetive:
            if self.X == i[0] and self.Y == i[1]:
                return True
        return False
    def move(self, tablero):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(tablero.mat)
        def valid(i):
            ConditionX = self.X + dx[i] < n and self.X + dx[i] >= 0
            ConditionY = self.Y + dy[i] < n and self.Y + dy[i] >= 0
            return ConditionY and ConditionX 
        
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

        
    def think(self, tablero):
        print("elige una opcion")
        print("1) mover")
        print("2) muro")
        print(self.NodeObjetive)
        opcion = input("--->")
        if opcion == "1":
            ans  = self.move(tablero)
            if self.Win():
                ans = True
            print(ans)
            return ans 
        if opcion == "2":
            print("muro")
            return 0 , 0
            #return setMuro()


#table = tablero(4, 4)
#table.createTable()
#HumanP = Human(0,4,4)
#HumanP.setXandSetY(3,2)
#HumanP.think(table)
