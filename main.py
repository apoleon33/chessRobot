import time

from chessBot import ChessBot
from chessEngine import ChessEngine
from conf import STOCKFISH_PATH_LINUX

engine = ChessEngine(STOCKFISH_PATH_LINUX, depth=20)
engine.stockfish.set_elo_rating(2000)
print(engine)
while True:
    time.sleep(0.5)
    engine.play()
    print(engine)

