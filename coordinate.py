from conf import log
from echiquier import Echiquier


class Coordinate:
    x: int
    y: int
    z: float

    # rotations en radians
    rx: float
    ry: float
    rz: float

    checkerXCoordinate: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def __init__(self, coord=None) -> None:
        """
        Créé un objet ``Coordinate`` à partie des coordonnées initiales passée en argument.
        :param coord: Une liste de ``float`` qui indique la position initiale de la forme ``[x,y,z,rx,ry,rz]``.
        """
        if coord is None:  # pas direct en argument pour éviter des problèmes de mutabilité
            coord = [0, 0, 0, 0, 0, 0]

        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]

        self.rx = coord[3]
        self.ry = coord[4]
        self.rz = coord[5]

    @property
    def case(self) -> str:
        """ Renvoie la case actuelle sur le plateau, par exemple ``a1``. """
        return f"{self.checkerXCoordinate[self.y]}{self.x}"

    @property
    def robotCoordinate(self) -> list[float]:
        """ Formate les coordonnées pour pouvoir directement les utiliser dans une commande de type ``moveL`` """
        log([Echiquier.xValues[self.x], Echiquier.yValues[self.y]])
        return [Echiquier.xValues[self.y], Echiquier.yValues[self.x], self.z, self.rx, self.ry, self.rz]

    @staticmethod
    def getIndexFromLetter(letter: str) -> int:
        """
        Récupère la place dans l'alphabet de la lettre passée en argument.
        :param letter:
        :return: L'indice de la lettre dans l'alphabet.
        """
        return ord(letter) - 96
