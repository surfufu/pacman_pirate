#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Intégration finale
Implémentation de la boucle principale du jeu avec tous les éléments
"""

import pygame
import sys
import os
from src.player import Player
from src.enemy import Enemy, Octopus, EnemyShip
from src.maze import Maze
from src.game_manager import GameManager
from src.level_manager import LevelManager
from src.maze_integration import create_maze_from_level, initialize_game_elements
from src.sound_manager import SoundManager
from src.menu_manager import MenuManager

class PacmanPirate:
    """Classe principale du jeu Pacman Pirate"""
    
    def __init__(self, width=800, height=672):
        """Initialisation du jeu
        
        Args:
            width (int, optional): Largeur de la fenêtre. Defaults to 800.
            height (int, optional): Hauteur de la fenêtre. Defaults to 672.
        """
        # Initialisation de Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Paramètres de base
        self.width = width
        self.height = height
        self.title = "Pacman Pirate"
        self.fps = 60
        self.cell_size = 32
        
        # Création de la fenêtre
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        
        # Gestionnaires
        self.level_manager = LevelManager()
        self.game_manager = GameManager(self.screen, self.fps)
        self.sound_manager = SoundManager()
        self.menu_manager = MenuManager(self.screen, self.sound_manager)
        
        # Éléments du jeu
        self.player = None
        self.enemies = []
        self.maze = None
        
        # État du jeu
        self.running = True
        self.game_state = "menu"  # menu, playing, pause, level_transition, game_over, victory
        self.current_level = 1
        self.score = 0
        self.lives = 3
        self.high_scores = []
        
        # Chargement des assets
        self.load_assets()
    
    def load_assets(self):
        """Charge les assets du jeu (images et sons)"""
        # Chemins des assets
        self.assets_dir = os.path.join(os.getcwd(), "assets")
        self.images_dir = os.path.join(self.assets_dir, "images")
        self.sounds_dir = os.path.join(self.assets_dir, "sounds")
        
        # Vérification des répertoires
        if not os.path.exists(self.images_dir):
            print(f"Répertoire d'images non trouvé: {self.images_dir}")
            return
        
        if not os.path.exists(self.sounds_dir):
            print(f"Répertoire de sons non trouvé: {self.sounds_dir}")
            return
        
        # Chargement des images
        self.images = {}
        image_files = {
            "player": "player.png",
            "octopus": "octopus.png",
            "enemy_ship": "enemy_ship.png",
            "wall": "wall.png",
            "point": "point.png",
            "power_point": "power_point.png"
        }
        
        for name, file in image_files.items():
            path = os.path.join(self.images_dir, file)
            try:
                if os.path.exists(path):
                    self.images[name] = pygame.image.load(path).convert_alpha()
                    print(f"Image {name} chargée: {path}")
                else:
                    print(f"Image {name} non trouvée: {path}")
                    # Créer une surface par défaut
                    self.images[name] = pygame.Surface((self.cell_size, self.cell_size))
                    if name == "player":
                        self.images[name].fill((255, 255, 0))  # Jaune
                    elif name == "octopus":
                        self.images[name].fill((128, 0, 128))  # Violet
                    elif name == "enemy_ship":
                        self.images[name].fill((255, 0, 0))  # Rouge
                    elif name == "wall":
                        self.images[name].fill((0, 0, 139))  # Bleu foncé
                    elif name == "point":
                        self.images[name] = pygame.Surface((8, 8))
                        self.images[name].fill((255, 215, 0))  # Or
                    elif name == "power_point":
                        self.images[name] = pygame.Surface((16, 16))
                        self.images[name].fill((255, 255, 255))  # Blanc
            except pygame.error as e:
                print(f"Erreur lors du chargement de l'image {name}: {e}")
                # Créer une surface par défaut
                self.images[name] = pygame.Surface((self.cell_size, self.cell_size))
                self.images[name].fill((255, 0, 255))  # Magenta (erreur)
        
        # Chargement des sons
        try:
            self.sound_manager.load_sounds(self.sounds_dir)
            
            # Chargement de la musique de fond
            background_music = os.path.join(self.sounds_dir, "background.wav")
            if os.path.exists(background_music) and os.path.getsize(background_music) > 100:
                self.sound_manager.play_music(background_music)
        except Exception as e:
            print(f"Erreur lors du chargement des sons: {e}")
    
    def initialize_level(self, level_number):
        """Initialise un niveau
        
        Args:
            level_number (int): Numéro du niveau
        """
        # Récupération des données du niveau
        level_data = self.level_manager.get_level(level_number)
        if not level_data:
            print(f"Niveau {level_number} non trouvé")
            return False
        
        # Création du labyrinthe et des éléments du jeu
        self.maze, player_start_pos, enemy_positions = initialize_game_elements(level_data, self.cell_size)
        
        # Création du joueur
        self.player = Player(player_start_pos[0], player_start_pos[1])
        self.player.image = self.images["player"]
        self.player.rect = self.player.image.get_rect(topleft=(player_start_pos[0], player_start_pos[1]))
        
        # Création des ennemis
        self.enemies = []
        for enemy_data in enemy_positions:
            enemy_type = enemy_data["type"]
            position = enemy_data["position"]
            
            if enemy_type == "octopus":
                enemy = Octopus(position[0], position[1])
                enemy.image = self.images["octopus"]
            else:  # ship
                enemy = EnemyShip(position[0], position[1])
                enemy.image = self.images["enemy_ship"]
            
            enemy.rect = enemy.image.get_rect(topleft=(position[0], position[1]))
            self.enemies.append(enemy)
        
        # Chargement des images pour le labyrinthe
        self.maze.wall_image = self.images["wall"]
        
        return True
    
    def handle_events(self):
        """Gère les événements du jeu"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state == "menu":
                        self.running = False
                    elif self.game_state == "playing":
                        self.game_state = "pause"
                        self.sound_manager.play_sound("menu")
                    elif self.game_state == "pause":
                        self.game_state = "playing"
                    else:
                        self.game_state = "menu"
                        self.sound_manager.play_sound("menu")
                
                elif event.key == pygame.K_SPACE:
                    if self.game_state == "menu":
                        # Afficher la transition de niveau avant de commencer
                        self.game_state = "level_transition"
                    elif self.game_state == "level_transition":
                        self.start_game()
                    elif self.game_state == "pause":
                        self.game_state = "playing"
                    elif self.game_state == "game_over":
                        self.current_level = 1
                        self.game_state = "level_transition"
                    elif self.game_state == "victory":
                        if self.current_level < self.level_manager.get_max_level():
                            self.current_level += 1
                            self.game_state = "level_transition"
                        else:
                            self.game_state = "menu"
                            self.sound_manager.play_sound("menu")
                
                elif event.key == pygame.K_m:
                    if self.game_state in ["game_over", "victory", "pause"]:
                        self.game_state = "menu"
                        self.sound_manager.play_sound("menu")
    
    def update(self):
        """Met à jour l'état du jeu"""
        if self.game_state == "playing":
            # Récupération des touches pressées
            keys = pygame.key.get_pressed()
            
            # Mise à jour du joueur
            old_x, old_y = self.player.x, self.player.y
            self.player.update(keys, self.maze)
            
            # Jouer le son de déplacement si le joueur a bougé
            if (self.player.x != old_x or self.player.y != old_y):
                self.sound_manager.play_sound("move")
            
            # Collecte des points
            points_collected = self.maze.collect_point(self.player.rect)
            if points_collected > 0:
                self.player.collect_point(points_collected)
                self.score += points_collected
                if points_collected > 1:
                    self.sound_manager.play_sound("power")
                else:
                    self.sound_manager.play_sound("collect")
            
            # Vérification de la victoire (tous les points collectés)
            if self.maze.is_complete():
                self.game_state = "victory"
                self.sound_manager.play_sound("victory")
            
            # Mise à jour des ennemis
            for enemy in self.enemies:
                enemy.update(self.maze, self.player)
                
                # Vérification des collisions avec le joueur
                if enemy.check_player_collision(self.player):
                    self.lives -= 1
                    self.sound_manager.play_sound("hit")
                    
                    if self.lives <= 0:
                        self.game_state = "game_over"
                        self.sound_manager.play_sound("game_over")
                    else:
                        # Repositionner le joueur
                        level_data = self.level_manager.get_level(self.current_level)
                        player_start_pos = level_data.get("player_start", (1, 1))
                        self.player.x = player_start_pos[0] * self.cell_size
                        self.player.y = player_start_pos[1] * self.cell_size
                        self.player.rect.topleft = (self.player.x, self.player.y)
    
    def draw(self):
        """Dessine les éléments du jeu sur l'écran"""
        # Effacement de l'écran
        self.screen.fill((0, 0, 128))  # Bleu foncé pour l'océan
        
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            # Dessin du labyrinthe
            self.maze.draw(self.screen)
            
            # Dessin des ennemis
            for enemy in self.enemies:
                enemy.draw(self.screen)
            
            # Dessin du joueur
            self.player.draw(self.screen)
            
            # Dessin du score et des vies
            self.draw_hud()
        elif self.game_state == "pause":
            # Dessin du jeu en arrière-plan
            self.maze.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
            self.player.draw(self.screen)
            self.draw_hud()
            
            # Dessin du menu de pause par-dessus
            self.draw_pause()
        elif self.game_state == "level_transition":
            self.draw_level_transition()
        elif self.game_state == "game_over":
            self.draw_game_over()
        elif self.game_state == "victory":
            self.draw_victory()
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
    
    def draw_menu(self):
        """Dessine le menu principal"""
        self.menu_manager.draw_main_menu(self.high_scores)
    
    def draw_hud(self):
        """Dessine l'interface utilisateur pendant le jeu"""
        # Score
        font = pygame.font.SysFont(None, 36)
        text_score = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text_score, (10, 10))
        
        # Vies
        text_lives = font.render(f"Vies: {self.lives}", True, (255, 255, 255))
        self.screen.blit(text_lives, (10, 50))
        
        # Niveau
        text_level = font.render(f"Niveau: {self.current_level}", True, (255, 255, 255))
        self.screen.blit(text_level, (10, 90))
    
    def draw_game_over(self):
        """Dessine l'écran de game over"""
        self.menu_manager.draw_game_over(self.score)
    
    def draw_victory(self):
        """Dessine l'écran de victoire"""
        is_final_level = self.current_level >= self.level_manager.get_max_level()
        self.menu_manager.draw_victory(self.score, is_final_level)
    
    def draw_pause(self):
        """Dessine le menu de pause"""
        self.menu_manager.draw_pause_menu()
    
    def draw_level_transition(self):
        """Dessine la transition entre les niveaux"""
        level_data = self.level_manager.get_level(self.current_level)
        level_name = level_data.get("name", f"Niveau {self.current_level}")
        self.menu_manager.draw_level_transition(self.current_level, level_name)
    
    def start_game(self):
        """Démarre une nouvelle partie"""
        self.game_state = "playing"
        self.score = 0
        self.lives = 3
        
        # Initialisation du niveau
        if not self.initialize_level(self.current_level):
            print(f"Erreur lors de l'initialisation du niveau {self.current_level}")
            self.game_state = "menu"
    
    def run(self):
        """Exécute la boucle principale du jeu"""
        while self.running:
            # Gestion des événements
            self.handle_events()
            
            # Mise à jour du jeu
            self.update()
            
            # Dessin du jeu
            self.draw()
            
            # Limitation de la vitesse
            self.clock.tick(self.fps)
        
        # Fermeture de Pygame
        pygame.quit()

if __name__ == "__main__":
    # Création et lancement du jeu
    game = PacmanPirate()
    game.run()
