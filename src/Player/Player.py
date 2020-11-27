class Player:
    def __init__(self, num, hTb):
        self.PlayerNum = num
        self.X = 0
        self.Y = 0
        self.xTb = hTb
        self.yTb = hTb 
        self.NodeObjetive = []
        self.Path = []
        print("me cree", num)
        

    def setXandSetY(self, posx, posy):
        self.X = posx
        self.Y = posy
        self.NodeObjetive = self.SearchObjectives(self.X, self.Y)

    def SearchObjectives(self, Xp, Yp):
        if Xp == 0 and (Yp >= 0 and Yp < self.yTb):
            Objetives = [(self.xTb - 1, y)for y in range(self.yTb)]

        elif Xp == self.xTb - 1 and (Yp >= 0 and Yp < self.yTb):
            Objetives = [(0, y)for y in range(self.yTb)]

        elif  (Xp >= 0 and Xp < self.xTb)and Yp == 0:
            Objetives = [(x, self.yTb - 1)for x in range(self.xTb)]

        elif (Xp >= 0 and Xp < self.xTb) and Yp == self.yTb - 1:
            Objetives = [(x, 0)for x in range(self.xTb)]

        return Objetives

    def Win(self):
        for i in self.NodeObjetive:
            if self.X == i[0] and self.Y == i[1]:
                return True
        return False
    def move(self,tablero):
        print("aqui me muevo")
    def setMuros(self,tablero):
        print("aqui pongo un muro")
    def think(self,tablero):
        print("aqui decido si pongo un muero o me muevo")
