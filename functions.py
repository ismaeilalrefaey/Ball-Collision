import pygame
import globalVar
from vpython import *


def cinemaView():
    scene.camera.up = vector(0, 0, -1)
    scene.camera.pos = vector(0, 0, 0)
    scene.camera.axis = vector(0, -globalVar.cameraConst, 0)
    i = 0
    while i < globalVar.cameraConst:
        rate(globalVar.frameRate)
        scene.camera.pos = vector(0, i, 0)
        i += 0.07
    i = 0
    while i < globalVar.cameraConst:
        rate(globalVar.frameRate)
        scene.camera.pos = vector(0, globalVar.cameraConst, i)
        scene.camera.axis = vector(0, -globalVar.cameraConst, -i)
        i += 0.07

def mulMat(mat, vel):
    res = vector(0, 0, 0)

    res.x = mat[0][0] * vel.x + mat[0][1] * vel.z
    res.z = mat[1][0] * vel.x + mat[1][1] * vel.z

    return res


def distance(x1, z1, x2, z2):
    return sqrt(abs(x2 - x1) ** 2 + abs(z2 - z1) ** 2)


def Run(btn):
    globalVar.state = not globalVar.state

    if globalVar.state:
        btn.text = "Pause"
    else:
        btn.text = "Run"
    return


def Mute(btn):
    globalVar.play = not globalVar.play
    if globalVar.play:
        btn.text = "Mute"
        pygame.mixer.music.unpause()
    else:
        btn.text = "Play"
        pygame.mixer.music.pause()

def stillMoving(elements):
    for i in elements:
        if i.move is not None:
            return True
    return False
