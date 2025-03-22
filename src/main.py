#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Jeu inspiré de Pacman sur un thème pirate
Fichier principal du jeu
"""

import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()  # Pour les sons

# Paramètres de base
TITLE = "Pacman Pirate"
WIDTH = 800
HEIGHT = 600
FPS = 60
CELL_SIZE = 32  # Taille d'une case du labyrinthe

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

def main():
    """Fonction principale du jeu"""
    running = True
    
    # Boucle principale du jeu
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Mise à jour du jeu
        
        # Affichage
        screen.fill(BLUE)  # Fond bleu pour représenter l'océan
        
        # Affichage d'un message temporaire
        font = pygame.font.SysFont(None, 36)
        text = font.render("Pacman Pirate - En développement", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
        
        # Contrôle de la vitesse du jeu
        clock.tick(FPS)
    
    # Nettoyage et fermeture
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
