from enum import Enum


class Echiquier(Enum):
    xValues = [0.539, 0.586, 0.630, 0.674, 0.721, 0.765, 0.808, 0.855]
    yValues = [0.033, -0.009, -0.054, -0.099, -0.141, -0.189, -0.234, -0.279]
    pieceTakenX = 0.695
    pieceTakenY = -0.357

    def __getitem__(self, item):
        return self.value[item - 1]