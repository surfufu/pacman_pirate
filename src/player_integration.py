#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module d'intégration du joueur
Intégration du joueur avec le labyrinthe et gestion des entrées
"""

import pygame
import sys
import os
from src.player import Player
from src.maze import Maze
from src.level_manager import LevelManager
from src.maze_integration import create_maze_from_level

def test_player_movement():
    """Teste le mouvement du joueur dans le labyrinthe"""
    # Initialisation de Pygame
    pygame.init()
    
    # Création de la fenêtre
    screen = pygame.display.set_mode((800, 672))
    pygame.display.set_caption("Test du joueur")
    
    # Création du gestionnaire de niveaux
    level_manager = LevelManager()
    
    # Récupération des données du niveau 1
    level_data = level_manager.get_level(1)
    
    # Création du labyrinthe
    maze = create_maze_from_level(level_data)
    
    # Position de départ du joueur
    player_start_pos = level_data.get("player_start", (1, 1))
    player_x = player_start_pos[0] * maze.cell_size
    player_y = player_start_pos[1] * maze.cell_size
    
    # Création du joueur
    player = Player(player_x, player_y)
    
    # Création d'une image temporaire pour le joueur
    player_image = pygame.Surface((maze.cell_size, maze.cell_size))
    player_image.fill((255, 255, 0))  # Jaune
    player.image = player_image
    player.rect = player_image.get_rect(topleft=(player_x, player_y))
    
    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    score = 0
    
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Récupération des touches pressées
        keys = pygame.key.get_pressed()
        
        # Mise à jour du joueur
        old_x, old_y = player.x, player.y
        player.update(keys, maze)
        
        # Collecte des points
        points_collected = maze.collect_point(player.rect)
        if points_collected > 0:
            score += points_collected
            print(f"Score: {score}")
        
        # Effacement de l'écran
        screen.fill((0, 0, 128))  # Bleu foncé pour l'océan
        
        # Dessin du labyrinthe
        maze.draw(screen)
        
        # Dessin du joueur
        player.draw(screen)
        
        # Affichage du score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
        
        # Limitation de la vitesse
        clock.tick(60)
    
    # Fermeture de Pygame
    pygame.quit()

if __name__ == "__main__":
    test_player_movement()
