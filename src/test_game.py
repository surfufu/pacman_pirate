#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module de test
Tests des fonctionnalités du jeu
"""

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Désactiver l'initialisation de l'audio pour les tests
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
from src.game import PacmanPirate

def test_game_initialization():
    """Teste l'initialisation du jeu"""
    print("Test d'initialisation du jeu...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Vérification des attributs
    assert game.width == 800, f"Largeur incorrecte: {game.width} au lieu de 800"
    assert game.height == 672, f"Hauteur incorrecte: {game.height} au lieu de 672"
    assert game.title == "Pacman Pirate", f"Titre incorrect: {game.title} au lieu de Pacman Pirate"
    assert game.fps == 60, f"FPS incorrect: {game.fps} au lieu de 60"
    assert game.cell_size == 32, f"Taille de cellule incorrecte: {game.cell_size} au lieu de 32"
    
    # Vérification des gestionnaires
    assert game.level_manager is not None, "LevelManager non initialisé"
    assert game.game_manager is not None, "GameManager non initialisé"
    assert game.sound_manager is not None, "SoundManager non initialisé"
    assert game.menu_manager is not None, "MenuManager non initialisé"
    
    # Vérification de l'état initial
    assert game.game_state == "menu", f"État initial incorrect: {game.game_state} au lieu de menu"
    assert game.current_level == 1, f"Niveau initial incorrect: {game.current_level} au lieu de 1"
    assert game.score == 0, f"Score initial incorrect: {game.score} au lieu de 0"
    assert game.lives == 3, f"Vies initiales incorrectes: {game.lives} au lieu de 3"
    
    print("Test d'initialisation réussi!")
    return True

def test_level_loading():
    """Teste le chargement des niveaux"""
    print("Test de chargement des niveaux...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Vérification des niveaux
    max_level = game.level_manager.get_max_level()
    assert max_level >= 1, f"Nombre de niveaux incorrect: {max_level}"
    
    # Test de chargement de chaque niveau
    for level in range(1, max_level + 1):
        level_data = game.level_manager.get_level(level)
        assert level_data is not None, f"Données du niveau {level} non trouvées"
        assert "layout" in level_data, f"Layout manquant dans le niveau {level}"
        assert "player_start" in level_data, f"Position de départ du joueur manquante dans le niveau {level}"
        assert "enemies" in level_data, f"Ennemis manquants dans le niveau {level}"
    
    # Test d'initialisation d'un niveau
    success = game.initialize_level(1)
    assert success, "Échec de l'initialisation du niveau 1"
    assert game.maze is not None, "Labyrinthe non initialisé"
    assert game.player is not None, "Joueur non initialisé"
    assert len(game.enemies) > 0, "Aucun ennemi initialisé"
    
    print("Test de chargement des niveaux réussi!")
    return True

def test_player_movement():
    """Teste le mouvement du joueur"""
    print("Test du mouvement du joueur...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Initialisation du niveau
    game.initialize_level(1)
    
    # Position initiale du joueur
    initial_x, initial_y = game.player.x, game.player.y
    
    # Simulation d'une touche pressée (droite)
    keys = {pygame.K_RIGHT: True, pygame.K_LEFT: False, pygame.K_UP: False, pygame.K_DOWN: False}
    game.player.update(keys, game.maze)
    
    # Vérification du mouvement
    assert game.player.x > initial_x, f"Le joueur ne s'est pas déplacé vers la droite: {game.player.x} <= {initial_x}"
    
    print("Test du mouvement du joueur réussi!")
    return True

def test_enemy_movement():
    """Teste le mouvement des ennemis"""
    print("Test du mouvement des ennemis...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Initialisation du niveau
    game.initialize_level(1)
    
    # Positions initiales des ennemis
    initial_positions = [(enemy.x, enemy.y) for enemy in game.enemies]
    
    # Mise à jour des ennemis
    for enemy in game.enemies:
        enemy.update(game.maze, game.player)
    
    # Vérification du mouvement
    current_positions = [(enemy.x, enemy.y) for enemy in game.enemies]
    moved = False
    for i, (initial, current) in enumerate(zip(initial_positions, current_positions)):
        if initial != current:
            moved = True
            break
    
    assert moved, "Aucun ennemi ne s'est déplacé"
    
    print("Test du mouvement des ennemis réussi!")
    return True

def test_collision_detection():
    """Teste la détection des collisions"""
    print("Test de la détection des collisions...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Initialisation du niveau
    game.initialize_level(1)
    
    # Forcer une collision entre le joueur et un ennemi
    if len(game.enemies) > 0:
        enemy = game.enemies[0]
        game.player.x = enemy.x
        game.player.y = enemy.y
        game.player.rect.topleft = (game.player.x, game.player.y)
        
        # Vérification de la collision
        assert enemy.check_player_collision(game.player), "Collision non détectée"
    
    print("Test de la détection des collisions réussi!")
    return True

def test_point_collection():
    """Teste la collecte des points"""
    print("Test de la collecte des points...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Initialisation du niveau
    game.initialize_level(1)
    
    # Nombre initial de points
    initial_points = len(game.maze.points)
    
    # Placer le joueur sur un point
    if len(game.maze.points) > 0:
        point = game.maze.points[0]
        game.player.x = point.x
        game.player.y = point.y
        game.player.rect.topleft = (game.player.x, game.player.y)
        
        # Collecte du point
        points_collected = game.maze.collect_point(game.player.rect)
        
        # Vérification de la collecte
        assert points_collected > 0, "Point non collecté"
        assert len(game.maze.points) < initial_points, "Nombre de points non mis à jour"
    
    print("Test de la collecte des points réussi!")
    return True

def test_game_states():
    """Teste les différents états du jeu"""
    print("Test des états du jeu...")
    
    # Initialisation de Pygame
    pygame.init()
    
    # Création du jeu
    game = PacmanPirate()
    
    # Vérification de l'état initial
    assert game.game_state == "menu", f"État initial incorrect: {game.game_state} au lieu de menu"
    
    # Changement d'état vers level_transition
    game.game_state = "level_transition"
    assert game.game_state == "level_transition", f"Changement d'état vers level_transition échoué: {game.game_state}"
    
    # Changement d'état vers playing
    game.start_game()
    assert game.game_state == "playing", f"Changement d'état vers playing échoué: {game.game_state}"
    
    # Changement d'état vers pause
    game.game_state = "pause"
    assert game.game_state == "pause", f"Changement d'état vers pause échoué: {game.game_state}"
    
    # Changement d'état vers game_over
    game.game_state = "game_over"
    assert game.game_state == "game_over", f"Changement d'état vers game_over échoué: {game.game_state}"
    
    # Changement d'état vers victory
    game.game_state = "victory"
    assert game.game_state == "victory", f"Changement d'état vers victory échoué: {game.game_state}"
    
    print("Test des états du jeu réussi!")
    return True

def run_all_tests():
    """Exécute tous les tests"""
    print("Exécution de tous les tests...")
    
    tests = [
        test_game_initialization,
        test_level_loading,
        test_player_movement,
        test_enemy_movement,
        test_collision_detection,
        test_point_collection,
        test_game_states
    ]
    
    success_count = 0
    for test in tests:
        try:
            if test():
                success_count += 1
        except Exception as e:
            print(f"Échec du test {test.__name__}: {e}")
    
    print(f"Tests terminés: {success_count}/{len(tests)} réussis")
    
    # Fermeture de Pygame
    pygame.quit()

if __name__ == "__main__":
    run_all_tests()
