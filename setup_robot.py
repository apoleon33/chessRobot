from chessEngine import ChessEngine
from conf import STOCKFISH_PATH_LINUX


def setupRobot():
    engine = ChessEngine(STOCKFISH_PATH_LINUX)
    engine.robot.start()
    engine.robot.close()

if __name__ == '__main__':
    setupRobot()
    print("setup complete")