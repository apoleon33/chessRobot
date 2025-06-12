import chessBot

robot = chessBot.ChessBot()
robot.start()

robot.goToCase("h1")
robot.goAtPieceHeight()
robot.close_gripper()
robot.resetHeight()
robot.goToCase("e1")
robot.goAtPieceHeight()
robot.open_gripper()
robot.resetHeight()

robot.close()
