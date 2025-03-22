#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module principal
Point d'entrée du jeu
"""

import os
import sys
from src.game import PacmanPirate

if __name__ == "__main__":
    # Assurons-nous que le répertoire de travail est correct
    if not os.path.exists("src"):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Création et lancement du jeu
    game = PacmanPirate()
    game.run()
