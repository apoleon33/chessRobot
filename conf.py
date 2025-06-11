# robot
ROBOT_IP = "192.168.12.126"

# pince
GRIPPER_IP = "192.168.12.244"
GRIPPER_PORT = 502
GRIPPER_MODEL = "rg6"

# misc
DEBUG = True
def log(text: str) -> None:
    """ N'affiche le message dans la console que si on est en mode debug"""
    if DEBUG:
        print(text)