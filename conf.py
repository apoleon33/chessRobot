# robot
ROBOT_IP = "192.168.12.126"

# pince
GRIPPER_IP = "192.168.12.244"
GRIPPER_PORT = 502
GRIPPER_MODEL = "rg6"

# chess engine
STOCKFISH_PATH = "libs/stockfish/stockfish-ubuntu-x86-64-avx2"
SAVE_FILE_PATH = "save.json"

# misc
DEBUG = True
ROBOT_ACTIVATED: bool = True # pour pouvoir tester plus facilement

def log(text) -> None:
    """ N'affiche le message dans la console que si on est en mode debug."""
    if DEBUG:
        print(text)
