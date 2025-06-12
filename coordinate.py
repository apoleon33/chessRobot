from conf import log, ECHIQUIER


class Coordinate:
    __x: int
    __y: int
    z: float

    # rotations en radians
    rx: float
    ry: float
    rz: float

    checkerXCoordinate: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]

    caseSize: float = 0.335 / len(checkerXCoordinate)  # largeur/hauteur d'une case (en m)

    def __init__(self, coord=None) -> None:
        """
        Créé un objet ``Coordinate`` à partie des coordonnées initiales passée en argument.
        :param coord: Une liste de ``float`` qui indique la position initiale de la forme ``[x,y,z,rx,ry,rz]``.
        """
        if coord is None:  # pas direct en argument pour éviter des problèmes de mutabilité
            coord = [0, 0, 0, 0, 0, 0]

        self.__x = coord[0]
        self.__y = coord[1]
        self.z = coord[2]

        self.rx = coord[3]
        self.ry = coord[4]
        self.rz = coord[5]

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @x.setter
    def x(self, x: int) -> None:
        self.__x = x

    @y.setter
    def y(self, y: int) -> None:
        self.__y = y

    @property
    def case(self) -> str:
        """ Renvoie la case actuelle sur le plateau, par exemple ``a1``. """
        return f"{self.checkerXCoordinate[self.__y]}{self.__x}"

    @property
    def robotCoordinate(self) -> list[float]:
        """ Formate les coordonnées pour pouvoir directement les utiliser dans une commande de type ``moveL`` """
        return [ECHIQUIER[self.__y][self.__x][0], ECHIQUIER[self.__y][self.__x][0], self.z, self.rx, self.ry, self.rz]

    @staticmethod
    def getIndexFromLetter(letter: str) -> int:
        """
        Récupère la place dans l'alphabet de la lettre passée en argument.
        :param letter:
        :return: L'indice de la lettre dans l'alphabet.
        """
        return ord(letter) - 96
