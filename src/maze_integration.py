#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module d'intégration du labyrinthe
Intégration de la structure du labyrinthe avec la classe Maze
"""

import pygame
from src.maze import Maze
from src.level_manager import LevelManager

def create_maze_from_level(level_data, cell_size=32):
    """Crée un labyrinthe à partir des données de niveau
    
    Args:
        level_data (dict): Données du niveau
        cell_size (int, optional): Taille d'une cellule en pixels. Defaults to 32.
        
    Returns:
        Maze: Instance de labyrinthe
    """
    layout = level_data["layout"]
    width = len(layout[0])
    height = len(layout)
    
    # Création du labyrinthe
    maze = Maze(width, height, cell_size)
    
    # Chargement du niveau
    maze.load_level(layout)
    
    return maze

def initialize_game_elements(level_data, cell_size=32):
    """Initialise les éléments du jeu à partir des données de niveau
    
    Args:
        level_data (dict): Données du niveau
        cell_size (int, optional): Taille d'une cellule en pixels. Defaults to 32.
        
    Returns:
        tuple: (maze, player_start_pos, enemy_positions)
    """
    # Création du labyrinthe
    maze = create_maze_from_level(level_data, cell_size)
    
    # Position de départ du joueur
    player_start_pos = level_data.get("player_start", (1, 1))
    player_start_pos = (player_start_pos[0] * cell_size, player_start_pos[1] * cell_size)
    
    # Positions des ennemis
    enemy_data = level_data.get("enemies", [])
    enemy_positions = []
    
    for enemy in enemy_data:
        enemy_type = enemy.get("type", "octopus")
        position = enemy.get("position", (1, 1))
        position = (position[0] * cell_size, position[1] * cell_size)
        enemy_positions.append({"type": enemy_type, "position": position})
    
    return maze, player_start_pos, enemy_positions

def test_maze_creation():
    """Teste la création du labyrinthe"""
    # Initialisation de Pygame
    pygame.init()
    
    # Création de la fenêtre
    screen = pygame.display.set_mode((800, 672))
    pygame.display.set_caption("Test du labyrinthe")
    
    # Création du gestionnaire de niveaux
    level_manager = LevelManager()
    
    # Récupération des données du niveau 1
    level_data = level_manager.get_level(1)
    
    # Création du labyrinthe
    maze, player_start_pos, enemy_positions = initialize_game_elements(level_data)
    
    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Effacement de l'écran
        screen.fill((0, 0, 128))  # Bleu foncé pour l'océan
        
        # Dessin du labyrinthe
        maze.draw(screen)
        
        # Dessin de la position de départ du joueur
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(player_start_pos[0], player_start_pos[1], 32, 32))
        
        # Dessin des positions des ennemis
        for enemy in enemy_positions:
            color = (255, 0, 0) if enemy["type"] == "ship" else (128, 0, 128)
            pygame.draw.rect(screen, color, pygame.Rect(enemy["position"][0], enemy["position"][1], 32, 32))
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
        
        # Limitation de la vitesse
        clock.tick(60)
    
    # Fermeture de Pygame
    pygame.quit()

if __name__ == "__main__":
    test_maze_creation()
