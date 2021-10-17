from abc import ABC

from Move.Move import Move
from Move.PureMove import PureMove
from functions import *


class BotMove(Move, ABC):
    def __init__(self, ball, vVec, h):
        super().__init__(vVec=vVec)
        self.ball = ball
        self.vVec = vVec
        diff = ball.radius - h
        vel = sqrt(vVec.x ** 2 + vVec.z ** 2)
        self.v = (diff * vel) / (2 * self.ball.radius)
        # vel = sqrt(vVec.x ** 2 + vVec.z ** 2)
        # self.v = vel - vel / (h * 5 / self.ball.radius)
        EkTot = 1 / 2 * self.ball.mass * vel ** 2
        self.Ek = 1 / 2 * self.ball.mass * self.v ** 2
        self.Id = (2.0 / 5.0) * self.ball.mass * self.ball.radius ** 2
        self.EkRot = EkTot - self.Ek
        self.w = -sqrt(2 * self.EkRot / self.Id)
        self.a = self.v / globalVar.frameRate
        if self.a * self.ball.mass <= self.ball.mass * globalVar.g * globalVar.fraction[self.ball.typeOfBall][globalVar.grid.typeOfGrid]:
            self.v = 0.0

    def __del__(self):
        pass

    def updateSpeed(self):
        if self.v <= 0.001 or self.w <= 0:
            self.ball.move = PureMove(ball=self.ball, vVec=self.vVec)
            self.__del__()
            return
        else:
            at = self.a / globalVar.frameRate
            Vf = self.v - at
            ratio = 100.0 - 100.0 * Vf / self.v
            self.vVec.x -= ratio * self.vVec.x / 100.0
            self.vVec.z -= ratio * self.vVec.z / 100.0
            self.v = Vf
            self.w -= ratio * self.w / 100.0
            return

    def move(self):
        if self.v <= 0.001 or self.w <= 0:
            self.ball.move = PureMove(ball=self.ball, vVec=self.vVec)
            self.__del__()
            return
        else:
            t = 1.0 / globalVar.frameRate

            self.ball.obj.pos.x += self.vVec.x * t
            self.ball.obj.pos.z += self.vVec.z * t
            self.v = sqrt(self.ball.move.vVec.x ** 2 + self.ball.move.vVec.z ** 2)
            self.w = self.v / self.ball.radius

            theta = self.w * t
            self.ball.obj.rotate(angle=-theta, axis=vector(self.vVec.z, 0, -self.vVec.x))
