#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module d'intégration des ennemis
Intégration des ennemis avec le labyrinthe et le joueur
"""

import pygame
import sys
import os
import random
from src.player import Player
from src.enemy import Enemy, Octopus, EnemyShip
from src.maze import Maze
from src.level_manager import LevelManager
from src.maze_integration import create_maze_from_level

def test_enemy_movement():
    """Teste le mouvement des ennemis dans le labyrinthe et leur interaction avec le joueur"""
    # Initialisation de Pygame
    pygame.init()
    
    # Création de la fenêtre
    screen = pygame.display.set_mode((800, 672))
    pygame.display.set_caption("Test des ennemis")
    
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
    
    # Création des ennemis
    enemies = []
    for enemy_data in level_data.get("enemies", []):
        enemy_type = enemy_data.get("type", "octopus")
        position = enemy_data.get("position", (1, 1))
        enemy_x = position[0] * maze.cell_size
        enemy_y = position[1] * maze.cell_size
        
        if enemy_type == "octopus":
            enemy = Octopus(enemy_x, enemy_y)
            enemy_image = pygame.Surface((maze.cell_size, maze.cell_size))
            enemy_image.fill((128, 0, 128))  # Violet
        else:  # ship
            enemy = EnemyShip(enemy_x, enemy_y)
            enemy_image = pygame.Surface((maze.cell_size, maze.cell_size))
            enemy_image.fill((255, 0, 0))  # Rouge
        
        enemy.image = enemy_image
        enemy.rect = enemy_image.get_rect(topleft=(enemy_x, enemy_y))
        enemies.append(enemy)
    
    # Boucle principale
    running = True
    clock = pygame.time.Clock()
    score = 0
    lives = 3
    game_over = False
    
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    # Réinitialisation du jeu
                    player.x = player_x
                    player.y = player_y
                    player.rect.topleft = (player_x, player_y)
                    score = 0
                    lives = 3
                    game_over = False
        
        if not game_over:
            # Récupération des touches pressées
            keys = pygame.key.get_pressed()
            
            # Mise à jour du joueur
            player.update(keys, maze)
            
            # Collecte des points
            points_collected = maze.collect_point(player.rect)
            if points_collected > 0:
                score += points_collected
            
            # Mise à jour des ennemis
            for enemy in enemies:
                enemy.update(maze, player)
                
                # Vérification des collisions avec le joueur
                if enemy.check_player_collision(player):
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                    else:
                        # Repositionner le joueur
                        player.x = player_x
                        player.y = player_y
                        player.rect.topleft = (player_x, player_y)
        
        # Effacement de l'écran
        screen.fill((0, 0, 128))  # Bleu foncé pour l'océan
        
        # Dessin du labyrinthe
        maze.draw(screen)
        
        # Dessin du joueur
        player.draw(screen)
        
        # Dessin des ennemis
        for enemy in enemies:
            enemy.draw(screen)
        
        # Affichage du score et des vies
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        lives_text = font.render(f"Vies: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 50))
        
        # Affichage du game over
        if game_over:
            game_over_text = font.render("GAME OVER - Appuyez sur ESPACE pour recommencer", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(game_over_text, game_over_rect)
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
        
        # Limitation de la vitesse
        clock.tick(60)
    
    # Fermeture de Pygame
    pygame.quit()

if __name__ == "__main__":
    test_enemy_movement()
