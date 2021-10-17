from Ball import *


class Grid:
    def __init__(self, length=30, width=30, typeOfGrid=0, elements=None):
        self.typeOfGrid = typeOfGrid
        if elements is None:
            elements = []
        self.elements = elements
        self.length = length
        self.width = width

        # typeOfGrid = 0
        if typeOfGrid == 0:
            self.obj = box(pos=vector(0, - globalVar.Radius / 4, 0), texture=textures.wood,
                           size=vector(self.length, globalVar.Radius / 2, self.width),
                           opacity=0.85, color=color.white)
        if typeOfGrid == 1:
            self.obj = box(pos=vector(0, - globalVar.Radius / 4, 0), texture=textures.metal,
                           size=vector(self.length, globalVar.Radius / 2, self.width),
                           opacity=0.85, color=color.white)
        if typeOfGrid == 2:
            self.obj = box(pos=vector(0, - globalVar.Radius / 4, 0), texture=textures.metal,
                           size=vector(self.length, globalVar.Radius / 2, self.width),
                           opacity=0.85, color=color.white)

        self.wallR = box(pos=vector(self.length / 2 + globalVar.Radius / 4, globalVar.Radius / 2, 0),
                         size=vector(globalVar.Radius / 2, 2 * globalVar.Radius, self.width + globalVar.Radius),
                         opacity=0.85,
                         texture=textures.wood)
        self.wallL = box(pos=vector(-self.length / 2 - globalVar.Radius / 4, globalVar.Radius / 2, 0),
                         size=vector(globalVar.Radius / 2, 2 * globalVar.Radius, self.width + globalVar.Radius),
                         opacity=0.85,
                         texture=textures.wood)
        self.wallD = box(pos=vector(0, globalVar.Radius / 2, self.width / 2 + globalVar.Radius / 4),
                         size=vector(self.length, 2 * globalVar.Radius, globalVar.Radius / 2), opacity=0.85,
                         texture=textures.wood)
        self.wallT = box(pos=vector(0, globalVar.Radius / 2, -self.width / 2 - globalVar.Radius / 4),
                         size=vector(self.length, 2 * globalVar.Radius, globalVar.Radius / 2), opacity=0.85,
                         texture=textures.wood)

    def lengthRandomizer(self):
        return random() * self.length - self.length / 2
        # a random number in Grid's length range

    def widthRandomizer(self):
        return random() * self.width - self.width / 2
        # a random number in Grid's width range

    def isInterfered(self, x, z):
        if self.elements is None:
            return False
        for ball in self.elements:
            if distance(x, z, ball.obj.pos.x, ball.obj.pos.z) < 2 * globalVar.Radius:
                return True
        return False

    def isOutside(self, x, z):
        return (x - globalVar.Radius < -self.length / 2) or (x + globalVar.Radius > self.length / 2) or (
                z - globalVar.Radius < -self.width / 2) or (z + globalVar.Radius > self.width / 2)

    def deployAnElement(self, numBall, vx, vz, p):
        randomTypeOfBall = int(random() * 4)

        # speedLimit = 100
        ball = Ball(position=vector(0, globalVar.Radius, 0), mass=10, radius=globalVar.Radius,
                    vVec=vector(vx, 0, vz), typeOfBall=randomTypeOfBall)
        self.elements.append(ball)

        i = 0
        while i < numBall - 1:
            randomTypeOfBall = int(random() * 3)
            x = self.lengthRandomizer()
            z = self.widthRandomizer()
            if not self.isInterfered(x, z) and not self.isOutside(x, z):
                h = 0
                if p == "Top":
                    h = 9 * globalVar.Radius / 5
                elif p == "Pure":
                    h = 7 * globalVar.Radius / 5
                elif p == "Middle":
                    h = 6 * globalVar.Radius / 5
                elif p == "Bottom":
                    h = 2 * globalVar.Radius / 5

                ball = Ball(position=vector(x, globalVar.Radius, z), mass=(5 + random() * 10),
                            radius=globalVar.Radius,
                            vVec=vector(0, 0, 0), typeOfBall=randomTypeOfBall, h=h)
                # (random() * 50) % speedLimit
                self.elements.append(ball)
                i += 1
