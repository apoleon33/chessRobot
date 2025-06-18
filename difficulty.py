from enum import Enum


class Difficulty(Enum):

    simon = (2, 200)
    beginner = (4, 700)
    intermediate = (10, 1200)
    advanced = (12, 1800)
    master = (15, 2200)


    @staticmethod
    def getDifficultyFromInput():
        difficultyOptions = ""
        for difficulty in Difficulty:
            difficultyOptions += f"- {difficulty}\n"
        return Difficulty[str(input(f"Choisissez la difficulté:\n{difficultyOptions}"))]

    @property
    def elo(self):
        return self.value[1]

    @property
    def depth(self):
        return self.value[0]

    def __str__(self):
        return f"{self.name} ({self.value[1]} elo)"