import time

import rtde_control

from conf import *
from libs.gripper import RG


class ChessBot:
    gripper: RG
    robot: rtde_control.RTDEControlInterface

    # Les coordonnées pour placer la pince au dessus de la case A1
    A1_COORDINATE: list[float] = [0.519, 0.041, -0.05, 2.32, -2.11, 0.0]

    # Largeur nécessaire à la pince pour entourer une pièce (en mm)
    PIECE_WIDTH: int = 330

    def __init__(self, gripper_model: str = GRIPPER_MODEL, gripper_ip=GRIPPER_IP, gripper_port=GRIPPER_PORT,
                 robot_ip=ROBOT_IP):
        self.gripper = RG(
            gripper=gripper_model,
            ip=gripper_ip,
            port=gripper_port,
        )

        self.robot = rtde_control.RTDEControlInterface(robot_ip)

    def start(self):
        """ Positionne le robot en A1 pour débuter la partie"""

        log("Lancement du robot, déplacement vers la case A1 et ouverture de la pince")

        self.robot.moveL(self.A1_COORDINATE, 0.5, 0.3) # à voir pour le 0.5 et 0.3
        self.open_gripper()

        log("Fin de la procédure 'start'")

    def open_gripper(self) -> None:
        """
        Ouvre la pince de la bonne largeur pour attraper une pièce.
        :return: None
        """
        log(f"Ouverture de la pince d'une largeur {self.PIECE_WIDTH}mm")
        self.gripper.move_gripper(self.PIECE_WIDTH)
        while self.gripper.get_status()[0]:
            time.sleep(0.5)
