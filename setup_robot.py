from chessEngine import ChessEngine
from conf import STOCKFISH_PATH_LINUX


def setupRobot():
    engine = ChessEngine(STOCKFISH_PATH_LINUX)
    engine.robot.start()
    input("attente de la prise de la pièce...")
    engine.robot.close_gripper()

    print("déplacement en a1")
    engine.robot.coordinate.z = -0.220
    engine.robot.goToCase("a1")



    input("attente vers déplacement en a8")
    engine.robot.goToCase("a8")
    input("attente")

if __name__ == '__main__':
    setupRobot()
    print("setup complete")