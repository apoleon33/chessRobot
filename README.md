<p align="center">
<img src="https://raw.githubusercontent.com/apoleon33/chessRobot/refs/heads/master/doc/header.png">
  <cite> Make a Universal Robot 5 play chess!</cite>
</p>

![](https://tokei.rs/b1/github/apoleon33/chessRobot) [![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![YouTube Video Views](https://img.shields.io/youtube/views/ng3PlrOtbL0?style=flat&logo=youtube&label=video%20demo&link=https%3A%2F%2Fyoutube.com%2Fshorts%2Fng3PlrOtbL0)](https://youtube.com/shorts/ng3PlrOtbL0) [![GitHub License](https://img.shields.io/github/license/apoleon33/chessRobot)](https://opensource.org/license/MIT)



> [!NOTE]  
> Projet créé dans le cadre des projets de fin d'année en 3ème année de junia ISEN année 2024-2025, catégorie robotique.

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
> Assurez vous d'être connecté au même réseau wifi que le robot UR, et que les paramètres réseau sont bien les bons dans `conf.py`, que vous êtes bien connecté au même réseau wifi que le UR, et que le robot est réglé en mode "remote".
> 
> Important de noter que les valeurs de l'échiquier (coordonnées de chaques cases etc) ne sont bonnes que dans le contexte dans lequel a été créé le projet, et il sera probablement nécessaire de modifier les valeurs dans le fichier `echiquier.py`.

## Calibration robot-échiquier

Afin d'aligner parfaitement l'échiquier avec les coordonnées stockées, utilisez ou bien `setup_robot.py`, ou si vous avez jupyter notebook d'installé, `setup_robot.ipynb`

## Lancement du programme
Éxécutez simplement `main.py` (testé avec python 3.10):

```bash
python3 main.py
```

# Remerciements
- [La librairie ur_rtde](https://gitlab.com/sdurobotics/ur_rtde), pour controler le robot.
- [onrobot-rg](https://github.com/takuya-ki/onrobot-rg), le seul code qui fonctionnait avec notre pince.
