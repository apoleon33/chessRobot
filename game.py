from chessEngine import ChessEngine
from conf import ROBOT_ACTIVATED, SAVE_FILE_PATH
from difficulty import Difficulty, DifficultyPreset
from save import Save


class Game:
    engine: ChessEngine
    save: Save

    def __init__(self, stockfish_path):
        self.engine = ChessEngine(stockfish_path)

        if ROBOT_ACTIVATED: self.engine.robot.start()

        self.selectGameMode()

    def selectGameMode(self):
        match int(input(
            "Veuillez choisir le mode de jeux:\n1. Nouvelle partie contre un humain \n2. Relancer la partie sauvegardée \n3. Partie à partir d'un FEN personnalisé \nVotre choix: ")):
            case 1:  # Nouvelle partie contre un humain
                colorChoice = int(input("Quelle couleur le robot joue-t-il? (1=blanc/2=noir): "))
                difficulty = DifficultyPreset.getDifficultyFromInput()
                self.engine.stockfish.set_elo_rating(difficulty.elo)
                self.engine.stockfish.set_depth(difficulty.depth)

                self.save = Save(SAVE_FILE_PATH, {
                    "FEN": self.engine.stockfish.get_fen_position(),
                    "evalBarEvolution": [],
                    "hasWhiteLastPLayed": False,
                    "isRobotWhite": colorChoice == 1,
                    "stockfishElo": difficulty.elo,
                    "stockfishDepth": difficulty.depth,
                })

                self.save.saveToFile()

                self.playAgainstAHuman(colorChoice == 1)

            case 2:
                self.save = Save.createFromSaveFile(SAVE_FILE_PATH)

                self.engine.stockfish.set_fen_position(self.save.fen)
                self.engine.stockfish.set_elo_rating(self.save.stockfishElo)
                print(
                    f"Dernière partie sauvegardée:\n{self.engine.stockfish.get_board_visual()}\nParamètres de la sauvegarde: {self.save}")

                if str(input("Voulez vous continuer cette partie? (y/n)")) == "y":
                    # la gueule de la condition
                    self.playAgainstAHuman((self.save.isRobotWhite and not self.save.hasWhiteLastPLayed) or (
                                not self.save.isRobotWhite and self.save.hasWhiteLastPLayed))

            case _:
                pass

    def playAgainstAHuman(self, isRobotWhite: bool):
        while True:
            print(self.engine)
            if isRobotWhite:
                self.engine.play()
                self.__updateSave(True)
                print(self.engine)

                isMoveLegal = False
                while not isMoveLegal:
                    isMoveLegal = self.engine.add_player_move(input("Entrez le coup joué par l'humain: "))
                    if not isMoveLegal:
                        print("Coup illégal détecté, veuillez entrer un coup correct.")

                self.__updateSave(False)

            else:
                isMoveLegal = False
                while not isMoveLegal:
                    isMoveLegal = self.engine.add_player_move(input("Entrez le coup joué par l'humain: "))
                    if not isMoveLegal:
                        print("Coup illégal détecté, veuillez entrer un coup correct.")

                self.__updateSave(True)
                print(self.engine)
                self.engine.play()
                self.__updateSave(False)

    def __updateSave(self, hasWhiteLastPLayed: bool):
        self.save.fen = self.engine.stockfish.get_fen_position()
        self.save.hasWhiteLastPLayed = not self.save.hasWhiteLastPLayed
        self.save.saveToFile()
