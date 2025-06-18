import time

import rtde_control
import rtde_receive

from conf import *
from coordinate import Coordinate
from echiquier import Echiquier
from libs.gripper import RG


class ChessBot:
    gripper: RG
    robot: rtde_control.RTDEControlInterface

    coordinate: Coordinate
    # Les coordonnées pour placer la pince au dessus de la case A1
    # 0.505, 0.049
    A1_COORDINATE: list[float] = [Echiquier.xValues[1], Echiquier.yValues[1], -0.05, 2.32, -2.11, 0.0]

    # Largeur nécessaire à la pince pour entourer une pièce (en mm)
    PIECE_WIDTH: int = 315
    # hauteur nécessaire pour prendre une pièce
    PIECE_HEIGHT: int = -0.225

    speed: float = 0.75
    acceleration: float = 1

    robot_ip:str

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

        self.robot_ip = robot_ip

    def start(self):
        """ Positionne le robot en A1 pour débuter la partie"""

        log("Lancement du robot, déplacement vers la case A1 et ouverture de la pince")

        self.robot.moveL(self.A1_COORDINATE, self.speed, self.acceleration)
        self.coordinate = Coordinate([0, 0, self.PIECE_HEIGHT, self.A1_COORDINATE[3], self.A1_COORDINATE[4],
                                      self.A1_COORDINATE[5]])  # synchronisé
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
        # time.sleep(1)

    def close_gripper(self) -> None:
        self.gripper.close_gripper()
        while self.gripper.get_status()[0]:
            time.sleep(0.5)
        # time.sleep(1)

    def __updateCoordinate(self):
        # rtde_c = rtde_control.RTDEControlInterface(self.robot_ip)
        rtde_r = rtde_receive.RTDEReceiveInterface(self.robot_ip)
        if rtde_r.isConnected() == False:
            log("déconnection détectée, reconnnexion...")
            rtde_r.reconnect()

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
        self.coordinate.x = Coordinate.getIndexFromLetter(case[0])
        self.coordinate.y = int(case[1])

        log(f"we go at {self.coordinate.robotCoordinate}")

        self.__updateCoordinate()

    def goToDumpster(self):
        self.robot.moveL([
            Echiquier.pieceTakenX.value,
            Echiquier.pieceTakenY.value,
            0.0,
            self.A1_COORDINATE[3],
            self.A1_COORDINATE[4],
            self.A1_COORDINATE[5]],
            self.speed,
            self.acceleration)

        self.robot.moveL([
            Echiquier.pieceTakenX.value,
            Echiquier.pieceTakenY.value,
            self.PIECE_HEIGHT,
            self.A1_COORDINATE[3],
            self.A1_COORDINATE[4],
            self.A1_COORDINATE[5]],
            self.speed,
            self.acceleration
        )
        self.gripper.move_gripper(self.PIECE_WIDTH)
        while self.gripper.get_status()[0]:
            time.sleep(0.5)
        self.robot.moveL([
            Echiquier.pieceTakenX.value,
            Echiquier.pieceTakenY.value,
            0.0,
            self.A1_COORDINATE[3],
            self.A1_COORDINATE[4],
            self.A1_COORDINATE[5]],
            self.speed,
            self.acceleration
        )

    def close(self):
        """ Déconnecte la pince et le robot """
        log("Closing connection...")
        self.gripper.close_connection()
        self.robot.disconnect()
