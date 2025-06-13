import stockfish
from stockfish import *
from conf import *

from chessBot import ChessBot


class ChessEngine:
    stockfish: Stockfish
    robot: ChessBot

    __robot_activate: bool = True # pour pouvoir tester plus facilement

    def __init__(self,
                 path: str,
                 gripper_model: str = GRIPPER_MODEL,
                 depth: int = 15,
                 gripper_ip=GRIPPER_IP,
                 gripper_port=GRIPPER_PORT,
                 robot_ip=ROBOT_IP):
        self.stockfish = Stockfish(path, depth=depth)

        if self.__robot_activate:
            self.robot = ChessBot(gripper_model, gripper_ip, gripper_port, robot_ip)
            self.robot.start()

    # TODO: play (ça fait jouer le robot), is_game_over

    def add_player_move(self, move: str):
        self.stockfish.make_moves_from_current_position([move])

    def is_move_a_capture(self, move: str) -> bool:
        """ Plus rapide que de tout re-taper."""
        return self.stockfish.will_move_be_a_capture(move) == self.stockfish.Capture.DIRECT_CAPTURE

    def play(self):
        bestMove = self.stockfish.get_best_move()
        startCase = bestMove[:2]
        endCase = bestMove[2:]
        log(f"Le meilleur mouvement est : {bestMove}")
        match self.stockfish.will_move_be_a_capture(bestMove):
            case self.stockfish.Capture.DIRECT_CAPTURE:
                log("capture détectée!")
                if self.__robot_activate:
                    # capture du pion et dépose dans la poubelle
                    self.robot.resetHeight()
                    self.robot.open_gripper()
                    self.robot.goToCase(endCase)
                    self.robot.goAtPieceHeight()
                    self.robot.close_gripper()
                    self.robot.resetHeight()
                    self.robot.goToDumpster()
                    self.robot.resetHeight()

                    # prise de la pièce
                    self.robot.resetHeight()
                    self.robot.open_gripper()
                    self.robot.goToCase(startCase)
                    self.robot.goAtPieceHeight()
                    self.robot.close_gripper()
                    self.robot.resetHeight()

                    # on la dépose dans la nouvelle case
                    self.robot.goToCase(endCase)
                    self.robot.goAtPieceHeight()
                    self.robot.open_gripper()
                    self.robot.resetHeight()

            case self.stockfish.Capture.NO_CAPTURE:
                # mouvement normal
                if self.__robot_activate:
                    # On prend la première pièce
                    self.robot.resetHeight()
                    self.robot.open_gripper()
                    self.robot.goToCase(startCase)
                    self.robot.goAtPieceHeight()
                    self.robot.close_gripper()
                    self.robot.resetHeight()

                    # on la dépose dans la nouvelle case
                    self.robot.goToCase(endCase)
                    self.robot.goAtPieceHeight()
                    self.robot.open_gripper()
                    self.robot.resetHeight()
                log(f"le robot a joué {bestMove}, en se déplaçant de {startCase} à {endCase}.")
            case self.stockfish.Capture.EN_PASSANT:
                log("en passant détecté!, pas implémenté pour le moment :)")


        self.stockfish.make_moves_from_current_position([bestMove])

    def __str__(self):
        return self.stockfish.get_board_visual()
