from enum import Enum

from conf import log


class Difficulty:
    elo: int = 33
    depth: int

    def __init__(self, elo=33, depth=10):
        self.elo = elo

        self.depth = depth

    @staticmethod
    def getDifficultyFromInput():
        return Difficulty(int(input("Entrez l'elo souhaité (compris entre 1320 et 3190): ")),
                          int(input("Entrez une profonder de calcul (entre 3 et 25): ")))

    def __str__(self):
        return f"(Elo: {self.elo}, depth: {self.depth})"


class DifficultyPreset(Enum):
    beginner = Difficulty(1320, 3)
    intermediate = Difficulty(1800, 10)
    master = Difficulty(2500, 19)
    terminator = Difficulty(3190, 25)

    @staticmethod
    def getDifficultyFromInput():
        print("Veuillez choisir un niveau de difficulté:")
        for i in DifficultyPreset:
            print(i)
        print("- custom")
        choice = str(input(" "))
        if choice != "custom":
            return DifficultyPreset[choice].value
        else:
            return Difficulty.getDifficultyFromInput()

    def __str__(self):
        return f"- {self.name}: {self.value}"
