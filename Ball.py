from Move.BotMove import BotMove
from Move.MidMove import MidMove
from Move.PureMove import *
from Move.TopMove import TopMove


class Ball:
    def __init__(self, position, mass, radius, vVec, typeOfBall=0, h=7 * globalVar.Radius / 5):
        self.typeOfBall = typeOfBall
        self.mass = float(mass)  # float
        self.radius = float(radius)  # float
        if vVec == vector(0, 0, 0):
            self.move = None
        else:
            if h < self.radius:
                self.move = BotMove(ball=self, vVec=vVec, h=h)
            elif h < 7 * self.radius / 5:
                self.move = MidMove(ball=self, vVec=vVec, h=h)
            elif h > 7 * self.radius / 5:
                self.move = TopMove(ball=self, vVec=vVec, h=h)
            else:
                self.move = PureMove(ball=self, vVec=vVec)

        # typeOfBall = 2
        if typeOfBall == 0:
            self.obj = sphere(pos=position, radius=self.radius, texture=textures.stones,
                              make_trail=True, retain=2.5)
        elif typeOfBall == 1:
            self.obj = sphere(pos=position, radius=self.radius, texture=textures.rug,
                              make_trail=True, retain=2.5)
        elif typeOfBall == 2:
            self.obj = sphere(pos=position, radius=self.radius, texture=textures.rough,
                              make_trail=True, retain=2.5)
        elif typeOfBall == 3:
            self.obj = sphere(pos=position, radius=self.radius, texture=textures.stucco,
                              make_trail=True, retain=2.5)
        elif typeOfBall == 4:
            self.obj = sphere(pos=position, radius=self.radius, texture=textures.rock,
                              make_trail=True, retain=2.5)

    def fixBallPosition(self, grid):
        if self.obj.pos.x + self.radius >= grid.wallR.pos.x - grid.wallR.size.x / 2:
            ss = self.obj.pos.x + self.radius - (grid.wallR.pos.x - grid.wallR.size.x / 2)
            if self.move is not None:
                self.move.vVec.x = -self.move.vVec.x
            self.obj.pos.x -= ss
        if self.obj.pos.x - self.radius <= grid.wallL.pos.x + grid.wallL.size.x / 2:
            ss = - self.obj.pos.x + self.radius + (grid.wallL.pos.x + grid.wallL.size.x / 2)
            if self.move is not None:
                self.move.vVec.x = -self.move.vVec.x
            self.obj.pos.x += ss
        if self.obj.pos.z + self.radius >= grid.wallD.pos.z - grid.wallD.size.z / 2:
            ss = self.obj.pos.z + self.radius - (grid.wallD.pos.z - grid.wallD.size.z / 2)
            if self.move is not None:
                self.move.vVec.z = -self.move.vVec.z
            self.obj.pos.z -= ss
        if self.obj.pos.z - self.radius <= grid.wallT.pos.z + grid.wallT.size.z / 2:
            ss = - self.obj.pos.z + self.radius + (grid.wallT.pos.z + grid.wallT.size.z / 2)
            if self.move is not None:
                self.move.vVec.z = -self.move.vVec.z
            self.obj.pos.z += ss
