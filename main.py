from win32api import GetSystemMetrics
from Collision import Collision
from Grid import *


def StartMain(width, length, ballsCount, radius, position, vx, vz):
    globalVar.Radius = float(radius)

    file = 'm.mp3'

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

    button(text="Pause", pos=scene.title_anchor, bind=Run, color=color.red)
    button(text="Mute", pos=scene.title_anchor, bind=Mute, color=color.red)
    globalVar.grid = Grid(length=int(length), width=int(width), typeOfGrid=int(random() * 3))

    globalVar.grid.deployAnElement(int(ballsCount), float(vx), float(vz), position)

    scene.autoScale = False
    sphere(pos=vec(0, 0, 0), radius=max(float(width), float(length)) * 4, texture="3.png", shininess=0)
    scene.range = 25
    scene.width = GetSystemMetrics(0)
    scene.height = GetSystemMetrics(1)

    sleep(1)

    cinemaView()
    while stillMoving(globalVar.grid.elements):
        rate(globalVar.frameRate)
        if globalVar.state:
            Collision.collisionDetection(grid=globalVar.grid)
            for i in globalVar.grid.elements:
                if i.move is not None:
                    i.move.updateSpeed()
                    if i.move is not None:
                        i.move.move()
                    i.fixBallPosition(grid=globalVar.grid)
