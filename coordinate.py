from conf import log


class Coordinate:
    initalCoordinate: list[float]
    __x: float
    __y: float
    z: float

    rx: float
    ry: float
    rz: float

    checkerXCoordinate: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]
    caseSize: float = 0.0425

    def __init__(self, coord: list[float]) -> None:
        self.initalCoordinate = coord
        self.__x = coord[0]
        self.__y = coord[1]
        self.z = coord[2]

        self.rx = coord[3]
        self.ry = coord[4]
        self.rz = coord[5]

    @property
    def case(self) -> str:
        """ Renvoie la case actuelle sur le plateau"""
        return f"{self.checkerXCoordinate[int((self.__x - self.initalCoordinate[0]) / self.caseSize)]}{int((self.__y - self.initalCoordinate[1]) / self.caseSize) + 1}"

    @property
    def x(self) -> float:
        return self.__x

    def changeX(self, newX:int) -> None:
        self.__x += newX * self.caseSize

    def changeY(self, newY:int) -> None:
        self.__y -= newY * self.caseSize

    @property
    def y(self) -> float:
        return self.__y

    @property
    def robotCoordinate(self) -> list[float]:
        return [self.__x, self.__y, self.z, self.rx, self.ry, self.rz]
