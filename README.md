<p align="center">
<img src="https://raw.githubusercontent.com/apoleon33/chessRobot/refs/heads/master/doc/header.png">
</p>

![](https://tokei.rs/b1/github/apoleon33/chessRobot) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/apoleon33/chessRobot) ![GitHub top language](https://img.shields.io/github/languages/top/apoleon33/chessRobot)

# Installation
- Clonez le repository:

```bash
git clone https://github.com/apoleon33/chessRobot.git
```

- Installez les dépendences nécessaires:
```bash
pip install -r requirements.txt
```

- Une fois ceci effectué, vous devez [télécharger la dernière version de stockfish](https://stockfishchess.org/download/), et la placer de préférence dans `libs/stockfish`.

- Faites ensuite correspondre la variable [`STOCKFISH_PATH`](https://github.com/apoleon33/chessRobot/blob/9d77c144684039ca7955af6fc029fc0b7ed8de45/conf.py#L10) au chemin vers l'executable stockfish.


# Lancement
> [!WARNING]  
> Assurez vous d'être connecté au même réseau wifi que le robot UR, et que les paramètres réseau sont bien les bons dans `conf.py`