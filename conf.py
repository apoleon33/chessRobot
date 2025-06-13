# robot
ROBOT_IP = "192.168.12.126"
ROBOT_ACTIVATED: bool = False # pour pouvoir tester plus facilement

# pince
GRIPPER_IP = "192.168.12.244"
GRIPPER_PORT = 502
GRIPPER_MODEL = "rg6"

# chess engine
STOCKFISH_PATH_LINUX = "libs/stockfish/stockfish-ubuntu-x86-64-avx2"

# misc
DEBUG = True


def log(text) -> None:
    """ N'affiche le message dans la console que si on est en mode debug"""
    if DEBUG:
        print(text)


# valeurs sur l'échiquier, inutile maintenant
ECHIQUIER: list[list[list[float]]] = [
    #       A               B               C               D                 E                 F               G               H
    [[0.539, 0.033], [0.540, -0.009], [0.541, -0.054], [0.541, -0.099], [0.541, -0.141], [0.540, -0.189],
     [0.544, -0.234], [0.543, -0.279]],  # 1
    [[0.586, 0.033], [0.586, -0.010], [0.587, -0.056], [0.587, -0.100], [0.587, -0.140], [], [], []],  # 2
    [0.630, 0.033],  # 3
    [0.674, 0.037],  # 4
    [0.721, 0.034],  # 5
    [0.765, 0.035],  # 6
    [0.808, 0.036],  # 7
    [0.855, 0.037]  # 8
]
