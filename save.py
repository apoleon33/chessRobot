import json

from stockfish import Stockfish

from conf import SAVE_FILE_PATH
from evalBar import EvalBar


class Save:
    file: str

    save: dict

    def __init__(self, file, initialSave: dict):
        self.file = file
        self.save = initialSave

    @staticmethod
    def createBlank(file: str = SAVE_FILE_PATH):
        return Save(file, {
            "FEN": "",
            "evalBarEvolution": [],
            "hasWhiteLastPLayed": False,
            "isRobotWhite": True,
            "stockfishElo": 1000,
            "stockfishDepth": 15,
        })

    @staticmethod
    def createFromStockfish(stockfish: Stockfish, file: str = SAVE_FILE_PATH, hasWhiteLastPLayed: bool = False,
                            isRobotWhite: bool = True, stockfishElo: int = 1000, stockfishDepth: int = 15):
        return Save(file, {
            "FEN": stockfish.get_fen_position(),
            "evalBarEvolution": [EvalBar(stockfish).score_normalized],
            "hasWhiteLastPLayed": hasWhiteLastPLayed,
            "isRobotWhite": isRobotWhite,
            "stockfishElo": stockfishElo,
            "stockfishDepth": stockfishDepth,
        })

    @staticmethod
    def createFromSaveFile(file: str = SAVE_FILE_PATH):
        with open(file, "r") as f:
            data = json.load(f)

        return Save(file, {
            "FEN": data["FEN"],
            "evalBarEvolution": data["evalBarEvolution"],
            "hasWhiteLastPLayed": data["hasWhiteLastPLayed"],
            "stockfishElo": data["stockfishElo"],
            "stockfishDepth": data["stockfishDepth"],
            "isRobotWhite": data["isRobotWhite"],
        })

    @property
    def fen(self) -> str:
        return self.save["FEN"]

    @fen.setter
    def fen(self, fen: str):
        self.save["FEN"] = fen

    @property
    def evalBarEvolution(self) -> list[EvalBar]:
        return self.save["evalBarEvolution"]

    @evalBarEvolution.setter
    def evalBarEvolution(self, evalBarEvolution: list[EvalBar]):
        self.save["evalBarEvolution"] = evalBarEvolution

    @property
    def hasWhiteLastPLayed(self) -> bool:
        return self.save["hasWhiteLastPLayed"]

    @hasWhiteLastPLayed.setter
    def hasWhiteLastPLayed(self, hasWhiteLastPLayer: bool):
        self.save["hasWhiteLastPLayed"] = hasWhiteLastPLayer

    @property
    def isRobotWhite(self) -> bool:
        return self.save["isRobotWhite"]

    @isRobotWhite.setter
    def isRobotWhite(self, isRobotWhite: bool):
        self.save["isRobotWhite"] = isRobotWhite

    @property
    def stockfishElo(self) -> int:
        return self.save["stockfishElo"]

    @stockfishElo.setter
    def stockfishElo(self, stockfishElo: int):
        self.save["stockfishElo"] = stockfishElo

    @property
    def stockfishDepth(self) -> int:
        return self.save["stockfishDepth"]

    @stockfishDepth.setter
    def stockfishDepth(self, stockfishDepth: int):
        self.save["stockfishDepth"] = stockfishDepth

    def saveToFile(self):
        with open(self.file, 'w') as file:
            json.dump(self.save, file, indent=4)

    def __str__(self):
        return str(self.save)
