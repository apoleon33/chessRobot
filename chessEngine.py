from stockfish import *
from conf import *

from chessBot import ChessBot
from evalBar import EvalBar


class ChessEngine:
    stockfish: Stockfish
    robot: ChessBot
    evalBar: EvalBar

    def __init__(self,
                 path: str,
                 gripper_model: str = GRIPPER_MODEL,
                 depth: int = 15,
                 gripper_ip=GRIPPER_IP,
                 gripper_port=GRIPPER_PORT,
                 robot_ip=ROBOT_IP):
        self.stockfish = Stockfish(
            path,
            depth=depth,
            parameters={
                "Threads": 7,
                "UCI_LimitStrength": "true",
            }
        )

        self.evalBar = EvalBar(self.stockfish)

        if ROBOT_ACTIVATED:
            self.robot = ChessBot(gripper_model, gripper_ip, gripper_port, robot_ip)
            self.robot.start()

    def add_player_move(self, move: str) -> bool:
        """
        Ajoute un coup joué par un humain.
        :param move: le mouvement joué (exemple: ``d2d4``)
        :return: ``True`` si le coup est légal (et a donc été ajouté à la liste de coups joués), ``False`` sinon
        """
        oldFen = self.stockfish.get_fen_position()
        self.stockfish.make_moves_from_current_position([move])
        return oldFen != self.stockfish.get_fen_position()

    def is_move_a_castle(self, move: str) -> bool:
        piece = self.stockfish.get_what_is_on_square(move[:2])

        white_castle = ['e1g1', 'e1c1']
        black_castle = ['e8g8', 'e8c8']
        # log(f"{move} test roque avec  et piece in white castle= {piece in white_castle} piece= {piece}")

        return (any(move in x for x in white_castle) and piece == self.stockfish.Piece.WHITE_KING) or (
                    any(move in x for x in black_castle) and piece == self.stockfish.Piece.BLACK_KING)

    def castle(self, move: str) -> None:
        towerMoves = {  # chaques mouvements de tour associé à chaques mouvements de rois
            'e1g1': "h1f1",
            'e1c1': "a1d1",
            'e8g8': "h8f8",
            'e8c8': "a8d8",
        }
        assert move in towerMoves.keys()
        self.movePiece(towerMoves[move][:2], towerMoves[move][2:])

    def play(self):
        bestMove = self.stockfish.get_best_move()
        startCase = bestMove[:2]
        endCase = bestMove[2:]
        log(f"Le meilleur mouvement est : {bestMove}")
        if not self.is_move_a_castle(bestMove):
            match self.stockfish.will_move_be_a_capture(bestMove):
                case self.stockfish.Capture.DIRECT_CAPTURE:
                    log("capture détectée!")
                    if ROBOT_ACTIVATED:
                        # capture du pion et dépose dans la poubelle
                        self.putPieceToThrash(endCase)
                        self.movePiece(startCase, endCase)

                case self.stockfish.Capture.NO_CAPTURE:
                    # mouvement normal
                    if ROBOT_ACTIVATED:
                        self.movePiece(startCase, endCase)
                    log(f"le robot a joué {bestMove}, en se déplaçant de {startCase} à {endCase}.")
                case self.stockfish.Capture.EN_PASSANT:
                    log("en passant détecté!")

                    if ROBOT_ACTIVATED:
                        self.robot.resetHeight()

                        # en partant du principe que stockfish donne les coordonnées de son pion
                        self.movePiece(startCase, endCase)
                        self.putPieceToThrash(f"{endCase[0]}{int(endCase[1]) - 1}")


        else:  # roque
            log("Roque detecté")
            self.movePiece(startCase, endCase)
            self.castle(bestMove)

        self.stockfish.make_moves_from_current_position([bestMove])
        return bestMove

    def movePiece(self, startCase: str, endCase: str) -> None:
        # On prend la pièce
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

    def putPieceToThrash(self, case: str):
        self.robot.resetHeight()
        self.robot.open_gripper()
        self.robot.goToCase(case)
        self.robot.goAtPieceHeight()
        self.robot.close_gripper()
        self.robot.resetHeight()
        self.robot.goToDumpster()
        self.robot.resetHeight()

    def __str__(self):
        return f"{self.stockfish.get_board_visual()}\n FEN position: {self.stockfish.get_fen_position()} \n {self.evalBar}"
