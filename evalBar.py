from stockfish import Stockfish


class EvalBar:
    stockfish: Stockfish

    MAX_CP = 500  # Seuil max pour la normalisation (ex: ±5 pions)
    BAR_WIDTH = 40  # Largeur de la barre en caractères

    def __init__(self, stockfish: Stockfish):
        self.stockfish = stockfish

    @property
    def score_normalized(self):
        eval_data = self.stockfish.get_evaluation()

        if eval_data["type"] == "cp":
            cp = eval_data["value"]
            white_advantage = cp >= 0
            abs_cp = abs(cp)

            # Formatage du texte (ex: "+1.50")
            text = f"{'+' if white_advantage else '-'}{abs_cp / 100:.2f}"

            # Normalisation entre [-1, 1] pour la barre
            normalized = max(-1, min(1, cp / self.MAX_CP))
            return text, normalized

        elif eval_data["type"] == "mate":
            mate_in = eval_data["value"]
            if mate_in > 0:
                return f"♔ Mat in {mate_in}", 1.0  # Blancs gagnent
            else:
                return f"♚ Mat in {abs(mate_in)}", -1.0  # Noirs gagnent

        return "0.00", 0.0

    def __str__(self) -> str:
        # Calcul des proportions
        text, score = self.score_normalized
        white_width = max(0, min(self.BAR_WIDTH, int((score + 1) * self.BAR_WIDTH / 2)))
        black_width = self.BAR_WIDTH - white_width

        # Barre
        white_part = "⬜" * white_width
        black_part = "⬛" * black_width

        return f"{white_part}{black_part} {text}"