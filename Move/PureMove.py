import math
from abc import ABC

from Move.Move import Move
from functions import *


class PureMove(Move, ABC):
    def __init__(self, ball, vVec):
        super().__init__(vVec=vVec)
        self.ball = ball
        self.v = sqrt(vVec.x ** 2 + vVec.z ** 2)
        self.w = self.v / self.ball.radius
        # self.w = self.w * 180.0 / math.pi
        self.a = self.v / globalVar.frameRate
        # if self.a * self.ball.mass <= self.ball.mass * globalVar.g * globalVar.fraction[self.ball.typeOfBall][globalVar.grid.typeOfGrid]:
        #     self.v = 0.0

    def __del__(self):
        pass

    def updateSpeed(self):
        if self.v <= 0.001:
            self.ball.move = None
            self.__del__()
            return

        Id = (2.0 * self.ball.mass * self.ball.radius ** 2) / 50.0
        # row
        S = 2 * math.pi * self.ball.radius ** 2
        Fd = (1.0 * globalVar.row * self.v * self.v * globalVar.C * S) / 2.0
        Fs = globalVar.fraction[self.ball.typeOfBall][globalVar.grid.typeOfGrid] * self.ball.mass * globalVar.g
        alpha = ((Fs + Fd) * self.ball.radius) / Id
        aa = alpha * self.ball.radius
        Vf = self.v - aa / globalVar.frameRate
        ratio = 100.0 - 100.0 * Vf / self.v
        self.vVec.x -= ratio * self.vVec.x / 100.0
        self.vVec.z -= ratio * self.vVec.z / 100.0
        self.v = Vf
        self.w = self.v / self.ball.radius
        # self.w = self.w * 180.0 / math.pi

    def move(self):
        if self.v <= 0.001:
            self.ball.move = None
            self.__del__()
            return
        t = 1.0 / globalVar.frameRate

        self.ball.obj.pos.x += self.vVec.x * t
        self.ball.obj.pos.z += self.vVec.z * t
        self.v = sqrt(self.ball.move.vVec.x ** 2 + self.ball.move.vVec.z ** 2)
        self.w = self.v / self.ball.radius

        theta = self.w * t
        self.ball.obj.rotate(angle=theta,
                             axis=vector(self.vVec.z, 0, -self.vVec.x))
