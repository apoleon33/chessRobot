from conf import log

class Coordinate:
    # les coordonnées du robot lorsqu'il est à (0,0,0) sur l'échiquier
    initalCoordinate: list[float]
    __x: float
    __y: float
    z: float

    rx: float
    ry: float
    rz: float

    checkerXCoordinate: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # TODO: en faire une variable par axe, et affiner la précision
    caseSize: float = 0.0425 # largeur/hauteur d'une case (en m)

    def __init__(self, coord=None) -> None:
        """
        Créé un objet ``Coordinate`` à partie des coordonnées initiales passée en argument.
        :param coord: une liste de ``float`` qui indique la position initiale de la forme ``[x,y,z,rx,ry,rz]``.
        """
        if coord is None: # pas direct en argument pour éviter des problèmes de mutabilité
            coord = [0, 0, 0, 0, 0, 0]

        self.initalCoordinate = coord
        self.__x = coord[0]
        self.__y = coord[1]
        self.z = coord[2]

        self.rx = coord[3]
        self.ry = coord[4]
        self.rz = coord[5]

    @property
    def case(self) -> str:
        """ Renvoie la case actuelle sur le plateau, par exemple `a1` """
        return f"{self.checkerXCoordinate[int((self.__y - self.initalCoordinate[1]) / self.caseSize)]}{int((self.__x - self.initalCoordinate[0]) / self.caseSize) + 1}"

    @property
    def x(self) -> float:
        return self.__x

    def changeX(self, newX: int) -> None:
        self.__x += newX * self.caseSize

    def changeY(self, newY: int) -> None:
        self.__y -= newY * self.caseSize

    @property
    def y(self) -> float:
        return self.__y

    @property
    def robotCoordinate(self) -> list[float]:
        """ Formate les coordonnées pour pouvoir directement les utiliser dans une commande de type ``moveL`` """
        return [self.__x, self.__y, self.z, self.rx, self.ry, self.rz]
