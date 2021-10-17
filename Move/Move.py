import abc

class Move(metaclass=abc.ABCMeta):
    def __init__(self, vVec):
        self.vVec = vVec

    @abc.abstractclassmethod
    def move(cls):
        pass

    @abc.abstractclassmethod
    def updateSpeed(cls):
        pass
