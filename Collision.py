import math

from Move.PureMove import PureMove
from functions import *


class Collision:
    def __init__(self, ball1, ball2):
        dz = float(abs(ball1.obj.pos.z - ball2.obj.pos.z))
        dx = float(abs(ball1.obj.pos.x - ball2.obj.pos.x))
        if dx < dz:
            self.state = 1
            if ball1.obj.pos.z > ball2.obj.pos.z:
                if ball2.obj.pos.x < ball1.obj.pos.x:
                    self.angle = -math.atan2(dx, dz)
                else:
                    self.angle = math.atan2(dx, dz)
            else:
                if ball1.obj.pos.x < ball2.obj.pos.x:
                    self.angle = -math.atan2(dx, dz)
                else:
                    self.angle = math.atan2(dx, dz)
        else:
            self.state = 2
            if ball1.obj.pos.x > ball2.obj.pos.x:
                if ball1.obj.pos.z < ball1.obj.pos.z:
                    self.angle = -math.atan2(dz, dx)
                else:
                    self.angle = math.atan2(dz, dx)
            else:
                if ball1.obj.pos.z < ball2.obj.pos.z:
                    self.angle = math.atan2(dz, dx)
                else:
                    self.angle = -math.atan2(dz, dx)

        self.ball1 = ball1
        self.ball2 = ball2
        self.transMat = [[math.cos(self.angle), math.sin(self.angle)], [-math.sin(self.angle), math.cos(self.angle)]]
        self.inTraMat = [[math.cos(self.angle), -math.sin(self.angle)], [math.sin(self.angle), math.cos(self.angle)]]

    def getColRes(self):
        if self.state == 1:
            self.getColXRes()
        elif self.state == 2:
            self.getColZRes()

    def getColZRes(self):
        if self.ball1.move is None and self.ball2.move is None:
            return

        rV1 = vector(0, 0, 0)
        rV2 = vector(0, 0, 0)
        if self.ball1.move is not None:
            rV1 = mulMat(self.transMat, self.ball1.move.vVec)
        if self.ball2.move is not None:
            rV2 = mulMat(self.transMat, self.ball2.move.vVec)

        d = distance(self.ball1.obj.pos.x, self.ball1.obj.pos.z,
                     self.ball2.obj.pos.x, self.ball2.obj.pos.z)
        overlap = 2.0 * self.ball1.radius - d + 0.01

        if self.ball1.move is None:
            if rV2.z < 0:
                self.ball2.obj.pos.z += overlap
            elif rV2.z > 0:
                self.ball2.obj.pos.z -= overlap
        elif self.ball2.move is None:
            if rV1.z < 0:
                self.ball1.obj.pos.z += overlap
            elif rV1.z > 0:
                self.ball1.obj.pos.z -= overlap
        else:
            if rV1.z < 0:
                self.ball1.obj.pos.z += overlap / 2
            elif rV1.z > 0:
                self.ball1.obj.pos.z -= overlap / 2
            if rV2.z < 0:
                self.ball2.obj.pos.z += overlap / 2
            elif rV2.z > 0:
                self.ball2.obj.pos.z -= overlap / 2

        sumMass = self.ball1.mass + self.ball2.mass
        rfv1z = ((self.ball1.mass - self.ball2.mass) * rV1.z + 2 * self.ball2.mass * rV2.z) / sumMass
        rfv2z = ((self.ball2.mass - self.ball1.mass) * rV2.z + 2 * self.ball1.mass * rV1.z) / sumMass

        rfv1 = vector(rV1.x, 0, rfv1z)
        rfv2 = vector(rV2.x, 0, rfv2z)

        fv1 = mulMat(self.inTraMat, rfv1)
        fv2 = mulMat(self.inTraMat, rfv2)

        if self.ball1.move is None:
            self.ball1.move = PureMove(ball=self.ball1, vVec=fv1)
        else:
            self.ball1.move.vVec = fv1

        if self.ball2.move is None:
            self.ball2.move = PureMove(ball=self.ball2, vVec=fv2)
        else:
            self.ball2.move.vVec = fv2

    def getColXRes(self):
        if self.ball1.move is None and self.ball2.move is None:
            return

        rV1 = vector(0, 0, 0)
        rV2 = vector(0, 0, 0)
        if self.ball1.move is not None:
            rV1 = mulMat(self.transMat, self.ball1.move.vVec)
        if self.ball2.move is not None:
            rV2 = mulMat(self.transMat, self.ball2.move.vVec)

        d = distance(self.ball1.obj.pos.x, self.ball1.obj.pos.z,
                     self.ball2.obj.pos.x, self.ball2.obj.pos.z)
        overlap = 2 * self.ball1.radius - d + 0.01

        if self.ball1.move is None:
            if rV2.x < 0:
                self.ball2.obj.pos.x += overlap
            elif rV2.x > 0:
                self.ball2.obj.pos.x -= overlap
        elif self.ball2.move is None:
            if rV1.x < 0:
                self.ball1.obj.pos.x += overlap
            elif rV1.x > 0:
                self.ball1.obj.pos.x -= overlap
        else:
            if rV1.x < 0:
                self.ball1.obj.pos.x += overlap / 2
            elif rV1.x > 0:
                self.ball1.obj.pos.x -= overlap / 2
            if rV2.x < 0:
                self.ball2.obj.pos.x += overlap / 2
            elif rV2.x > 0:
                self.ball2.obj.pos.x -= overlap / 2

        sumMass = self.ball1.mass + self.ball2.mass
        rfv1x = ((self.ball1.mass - self.ball2.mass) * rV1.x + 2 * self.ball2.mass * rV2.x) / sumMass
        rfv2x = ((self.ball2.mass - self.ball1.mass) * rV2.x + 2 * self.ball1.mass * rV1.x) / sumMass

        rfv1 = vector(rfv1x, 0, rV1.z)
        rfv2 = vector(rfv2x, 0, rV2.z)

        fv1 = mulMat(self.inTraMat, rfv1)
        fv2 = mulMat(self.inTraMat, rfv2)

        if self.ball1.move is None:
            self.ball1.move = PureMove(ball=self.ball1, vVec=fv1)
        else:
            self.ball1.move.vVec = fv1

        if self.ball2.move is None:
            self.ball2.move = PureMove(ball=self.ball2, vVec=fv2)
        else:
            self.ball2.move.vVec = fv2

    @staticmethod
    def collisionDetection(grid):
        for i in range(0, len(grid.elements)):
            for j in range(i + 1, len(grid.elements)):
                d = distance(grid.elements[i].obj.pos.x, grid.elements[i].obj.pos.z,
                             grid.elements[j].obj.pos.x, grid.elements[j].obj.pos.z)
                minDist = 2 * grid.elements[i].radius

                if d <= minDist:
                    collision = Collision(grid.elements[i], grid.elements[j])
                    collision.getColRes()
                    break
