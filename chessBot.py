import time

import rtde_control

from conf import *
from coordinate import Coordinate
from libs.gripper import RG


class ChessBot:
    gripper: RG
    robot: rtde_control.RTDEControlInterface

    coordinate: Coordinate
    # Les coordonnées pour placer la pince au dessus de la case A1
    A1_COORDINATE: list[float] = [0.505, 0.049, -0.05, 2.32, -2.11, 0.0]

    # Largeur nécessaire à la pince pour entourer une pièce (en mm)
    PIECE_WIDTH: int = 315
    # hauteur nécessaire pour prendre une pièce
    PIECE_HEIGHT: int = -0.225

    speed: float = 0.5
    acceleration: float = 0.3

    def __init__(self,
                 gripper_model: str = GRIPPER_MODEL,
                 gripper_ip=GRIPPER_IP,
                 gripper_port=GRIPPER_PORT,
                 robot_ip=ROBOT_IP
                 ):
        """
        Créé un objet ``ChessBot`` à partir des informations sur la pince et le robot données en argument.
        :param gripper_model:
        :param gripper_ip:
        :param gripper_port:
        :param robot_ip:
        """
        self.gripper = RG(
            gripper=gripper_model,
            ip=gripper_ip,
            port=gripper_port,
        )

        self.robot = rtde_control.RTDEControlInterface(robot_ip)

        self.coordinate = Coordinate()  # pas synchronisé avec le robot à ce moment là du code

    def start(self):
        """ Positionne le robot en A1 pour débuter la partie"""

        log("Lancement du robot, déplacement vers la case A1 et ouverture de la pince")

        self.robot.moveL(self.A1_COORDINATE, self.speed, self.acceleration)
        self.coordinate = Coordinate(self.A1_COORDINATE)  # synchronisé
        self.open_gripper()

        log("Fin de la procédure 'start'")

    def open_gripper(self) -> None:
        """
        Ouvre la pince de la bonne largeur pour attraper une pièce.
        :return: ``None``
        """
        log(f"Ouverture de la pince d'une largeur {self.PIECE_WIDTH}mm")
        self.gripper.move_gripper(self.PIECE_WIDTH)
        while self.gripper.get_status()[0]:
            time.sleep(0.5)

    def close_gripper(self) -> None:
        self.gripper.close_gripper()
        while self.gripper.get_status()[0]:
            time.sleep(0.5)

    def __updateCoordinate(self):
        self.robot.moveL(self.coordinate.robotCoordinate, self.speed, self.acceleration)

    def goAtPieceHeight(self):
        self.coordinate.z = self.PIECE_HEIGHT
        self.__updateCoordinate()

    def resetHeight(self):
        self.coordinate.z = self.A1_COORDINATE[2]
        self.__updateCoordinate()

    def goToCase(self, case: str) -> None:
        """
        Se déplace en direction de la case, sans changer l'axe z.
        :param case: la case vers laquelle aller, de la forme ``yx`` (ex: ``c3``)
        """
        self.coordinate.x = Coordinate.getIndexFromLetter(case[0]) - 1
        self.coordinate.y = int(case[1]) - 1

        self.__updateCoordinate()

    def close(self):
        """ Déconnecte la pince et le robot """
        log("Closing connection...")
        self.gripper.close_connection()
        self.robot.disconnect()
