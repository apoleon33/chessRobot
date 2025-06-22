from enum import Enum

from conf import log


class Difficulty:
    #    # PLAYER             :  RATING  ERROR  POINTS  PLAYED   (%)
    #    1 master-skill-19    :  3191.1   40.4   940.0    1707    55
    #    2 master-skill-18    :  3170.3   39.3  1343.0    2519    53
    #    3 master-skill-17    :  3141.3   37.8  2282.0    4422    52
    #    4 master-skill-16    :  3111.2   37.1  2773.0    5423    51
    #    5 master-skill-15    :  3069.5   37.2  2728.5    5386    51
    #    6 master-skill-14    :  3024.8   36.1  2702.0    5339    51
    #    7 master-skill-13    :  2972.9   35.4  2645.5    5263    50
    #    8 master-skill-12    :  2923.1   35.0  2653.5    5165    51
    #    9 master-skill-11    :  2855.5   33.6  2524.0    5081    50
    #   10 master-skill-10    :  2788.3   32.0  2724.5    5511    49
    #   11 stash-bot-v25.0    :  2744.0   31.5  1952.5    3840    51
    #   12 master-skill-9     :  2702.8   30.5  2670.0    5018    53
    #   13 master-skill-8     :  2596.2   28.5  2669.5    4975    54
    #   14 stash-bot-v21.0    :  2561.2   30.0  1338.0    3366    40
    #   15 master-skill-7     :  2499.5   28.5  1934.0    4178    46
    #   16 stash-bot-v20.0    :  2452.6   27.7  1606.5    3378    48
    #   17 stash-bot-v19.0    :  2425.3   26.7  1787.0    3365    53
    #   18 master-skill-6     :  2363.2   26.4  2510.5    4379    57
    #   19 stash-bot-v17.0    :  2280.7   25.4  2209.0    4378    50
    #   20 master-skill-5     :  2203.7   25.3  2859.5    5422    53
    #   21 stash-bot-v15.3    :  2200.0   25.4  1757.0    4383    40
    #   22 stash-bot-v14      :  2145.9   25.5  2890.0    5167    56
    #   23 stash-bot-v13      :  2042.7   25.8  2263.5    4363    52
    #   24 stash-bot-v12      :  1963.4   25.8  1769.5    4210    42
    #   25 master-skill-4     :  1922.9   25.9  2690.0    5399    50
    #   26 stash-bot-v11      :  1873.0   26.3  2203.5    4335    51
    #   27 stash-bot-v10      :  1783.8   27.8  2568.5    4301    60
    #   28 master-skill-3     :  1742.3   27.8  1909.5    4439    43
    #   29 master-skill-2     :  1608.4   29.4  2064.5    4389    47
    #   30 stash-bot-v9       :  1582.6   30.2  2130.0    4230    50
    #   31 master-skill-1     :  1467.6   31.3  2015.5    4244    47
    #   32 stash-bot-v8       :  1452.8   31.5  1953.5    3780    52
    #   33 master-skill-0     :  1320.1   32.9   651.5    2083    31

    level: int = 33
    depth: int

    def __init__(self, difficulty=33, depth=10):
        self.level = difficulty

        self.depth = depth

    @staticmethod
    def getDifficultyFromInput():
        return Difficulty(int(input("Entrez un niveau de difficulté (33 -> 1320 elo, 1-> 3100 elo): ")), int(input("Entrez une profonder de calcul (entre 3 et 25): ")))

    def __str__(self):
        return f"(Difficulty level: {self.level}, depth: {self.depth})"


class DifficultyPreset(Enum):
    beginner = Difficulty(33, 3)
    intermediate = Difficulty(26, 10)
    master = Difficulty(11, 19)
    terminator = Difficulty(1, 25)

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


