#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module GameManager
Gestion globale du jeu, des scores et des niveaux
"""

import pygame
import os
import json

class GameManager:
    """Classe gérant l'ensemble du jeu"""
    
    def __init__(self, screen, fps=60):
        """Initialisation du gestionnaire de jeu
        
        Args:
            screen (Surface): Surface d'affichage principale
            fps (int, optional): Images par seconde. Defaults to 60.
        """
        self.screen = screen
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "menu"  # menu, playing, game_over, victory
        self.current_level = 1
        self.max_level = 3
        self.score = 0
        self.high_scores = self.load_high_scores()
        
        # Éléments du jeu
        self.player = None
        self.enemies = []
        self.maze = None
        
        # Sons et musique
        self.sounds = {}
        self.music_playing = False
    
    def load_high_scores(self, filename="high_scores.json"):
        """Charge les meilleurs scores depuis un fichier
        
        Args:
            filename (str, optional): Nom du fichier. Defaults to "high_scores.json".
            
        Returns:
            list: Liste des meilleurs scores
        """
        try:
            file_path = os.path.join("assets", filename)
            with open(file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Retourner une liste vide si le fichier n'existe pas ou est invalide
            return []
    
    def save_high_scores(self, filename="high_scores.json"):
        """Sauvegarde les meilleurs scores dans un fichier
        
        Args:
            filename (str, optional): Nom du fichier. Defaults to "high_scores.json".
        """
        file_path = os.path.join("assets", filename)
        with open(file_path, "w") as f:
            json.dump(self.high_scores, f)
    
    def add_high_score(self, score):
        """Ajoute un score à la liste des meilleurs scores
        
        Args:
            score (int): Score à ajouter
        """
        self.high_scores.append(score)
        self.high_scores.sort(reverse=True)
        # Garder seulement les 5 meilleurs scores
        self.high_scores = self.high_scores[:5]
        self.save_high_scores()
    
    def load_sounds(self, sound_paths):
        """Charge les sons du jeu
        
        Args:
            sound_paths (dict): Dictionnaire des chemins des sons
        """
        for name, path in sound_paths.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
            except pygame.error as e:
                print(f"Impossible de charger le son {name}: {e}")
    
    def play_sound(self, name):
        """Joue un son
        
        Args:
            name (str): Nom du son à jouer
        """
        if name in self.sounds:
            self.sounds[name].play()
    
    def play_music(self, music_path, loops=-1):
        """Joue la musique de fond
        
        Args:
            music_path (str): Chemin de la musique
            loops (int, optional): Nombre de répétitions (-1 pour infini). Defaults to -1.
        """
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(loops)
            self.music_playing = True
        except pygame.error as e:
            print(f"Impossible de charger la musique: {e}")
            self.music_playing = False
    
    def stop_music(self):
        """Arrête la musique de fond"""
        pygame.mixer.music.stop()
        self.music_playing = False
    
    def init_level(self, level_number):
        """Initialise un niveau
        
        Args:
            level_number (int): Numéro du niveau à initialiser
        """
        # Cette méthode sera implémentée plus tard avec les données des niveaux
        pass
    
    def update(self):
        """Met à jour l'état du jeu"""
        if self.game_state == "playing":
            # Mise à jour du joueur
            if self.player:
                keys = pygame.key.get_pressed()
                self.player.update(keys, self.maze)
                
                # Collecte des points
                if self.maze:
                    points = self.maze.collect_point(self.player.rect)
                    if points > 0:
                        self.player.collect_point(points)
                        self.score += points
                        self.play_sound("collect")
                
                # Vérification de la victoire (tous les points collectés)
                if self.maze and self.maze.is_complete():
                    self.game_state = "victory"
                    self.play_sound("victory")
            
            # Mise à jour des ennemis
            for enemy in self.enemies:
                enemy.update(self.maze, self.player)
                
                # Vérification des collisions avec le joueur
                if enemy.check_player_collision(self.player):
                    if not self.player.lose_life():
                        self.game_state = "game_over"
                        self.play_sound("game_over")
                    else:
                        self.play_sound("hit")
                        # Repositionner le joueur et les ennemis
                        self.reset_positions()
    
    def reset_positions(self):
        """Réinitialise les positions du joueur et des ennemis"""
        # Cette méthode sera implémentée plus tard
        pass
    
    def draw(self):
        """Dessine les éléments du jeu sur l'écran"""
        # Effacer l'écran
        self.screen.fill((0, 0, 128))  # Bleu foncé pour l'océan
        
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            # Dessiner le labyrinthe
            if self.maze:
                self.maze.draw(self.screen)
            
            # Dessiner les ennemis
            for enemy in self.enemies:
                enemy.draw(self.screen)
            
            # Dessiner le joueur
            if self.player:
                self.player.draw(self.screen)
            
            # Dessiner le score et les vies
            self.draw_hud()
        elif self.game_state == "game_over":
            self.draw_game_over()
        elif self.game_state == "victory":
            self.draw_victory()
        
        # Rafraîchir l'écran
        pygame.display.flip()
        
        # Contrôler la vitesse du jeu
        self.clock.tick(self.fps)
    
    def draw_menu(self):
        """Dessine le menu principal"""
        # Titre
        font_title = pygame.font.SysFont(None, 72)
        text_title = font_title.render("Pacman Pirate", True, (255, 215, 0))  # Or
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(text_title, text_rect_title)
        
        # Options du menu
        font_menu = pygame.font.SysFont(None, 36)
        
        # Jouer
        text_play = font_menu.render("Appuyez sur ESPACE pour jouer", True, (255, 255, 255))
        text_rect_play = text_play.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_play, text_rect_play)
        
        # Quitter
        text_quit = font_menu.render("Appuyez sur ÉCHAP pour quitter", True, (255, 255, 255))
        text_rect_quit = text_quit.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(text_quit, text_rect_quit)
        
        # Meilleurs scores
        text_scores = font_menu.render("Meilleurs scores:", True, (255, 255, 255))
        text_rect_scores = text_scores.get_rect(center=(self.screen.get_width() // 2, 450))
        self.screen.blit(text_scores, text_rect_scores)
        
        # Afficher les meilleurs scores
        for i, score in enumerate(self.high_scores[:5]):
            text_score = font_menu.render(f"{i+1}. {score}", True, (255, 255, 255))
            text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 500 + i * 40))
            self.screen.blit(text_score, text_rect_score)
    
    def draw_hud(self):
        """Dessine l'interface utilisateur pendant le jeu"""
        # Score
        font = pygame.font.SysFont(None, 36)
        text_score = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text_score, (10, 10))
        
        # Vies
        text_lives = font.render(f"Vies: {self.player.lives}", True, (255, 255, 255))
        self.screen.blit(text_lives, (10, 50))
        
        # Niveau
        text_level = font.render(f"Niveau: {self.current_level}", True, (255, 255, 255))
        self.screen.blit(text_level, (10, 90))
    
    def draw_game_over(self):
        """Dessine l'écran de game over"""
        # Titre
        font_title = pygame.font.SysFont(None, 72)
        text_title = font_title.render("Game Over", True, (255, 0, 0))  # Rouge
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(text_title, text_rect_title)
        
        # Score
        font_score = pygame.font.SysFont(None, 48)
        text_score = font_score.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_score, text_rect_score)
        
        # Rejouer
        font_menu = pygame.font.SysFont(None, 36)
        text_play = font_menu.render("Appuyez sur ESPACE pour rejouer", True, (255, 255, 255))
        text_rect_play = text_play.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(text_play, text_rect_play)
        
        # Menu
        text_menu = font_menu.render("Appuyez sur M pour retourner au menu", True, (255, 255, 255))
        text_rect_menu = text_menu.get_rect(center=(self.screen.get_width() // 2, 450))
        self.screen.blit(text_menu, text_rect_menu)
    
    def draw_victory(self):
        """Dessine l'écran de victoire"""
        # Titre
        font_title = pygame.font.SysFont(None, 72)
        text_title = font_title.render("Victoire !", True, (0, 255, 0))  # Vert
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(text_title, text_rect_title)
        
        # Score
        font_score = pygame.font.SysFont(None, 48)
        text_score = font_score.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_score, text_rect_score)
        
        # Niveau suivant ou fin
        font_menu = pygame.font.SysFont(None, 36)
        if self.current_level < self.max_level:
            text_next = font_menu.render("Appuyez sur ESPACE pour le niveau suivant", True, (255, 255, 255))
            text_rect_next = text_next.get_rect(center=(self.screen.get_width() // 2, 400))
            self.screen.blit(text_next, text_rect_next)
        else:
            text_end = font_menu.render("Félicitations ! Vous avez terminé le jeu !", True, (255, 255, 255))
            text_rect_end = text_end.get_rect(center=(self.screen.get_width() // 2, 400))
            self.screen.blit(text_end, text_rect_end)
        
        # Menu
        text_menu = font_menu.render("Appuyez sur M pour retourner au menu", True, (255, 255, 255))
        text_rect_menu = text_menu.get_rect(center=(self.screen.get_width() // 2, 450))
        self.screen.blit(text_menu, text_rect_menu)
    
    def handle_events(self):
        """Gère les événements du jeu
        
        Returns:
            bool: False si le jeu doit se terminer, True sinon
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state == "menu":
                        return False
                    else:
                        self.game_state = "menu"
                
                if event.key == pygame.K_SPACE:
                    if self.game_state == "menu":
                        self.start_game()
                    elif self.game_state == "game_over":
                        self.start_game()
                    elif self.game_state == "victory":
                        if self.current_level < self.max_level:
                            self.current_level += 1
                            self.start_game()
                        else:
                            self.game_state = "menu"
                
                if event.key == pygame.K_m:
                    if self.game_state in ["game_over", "victory"]:
                        self.game_state = "menu"
        
        return True
    
    def start_game(self):
        """Démarre une nouvelle partie"""
        self.game_state = "playing"
        self.score = 0
        self.init_level(self.current_level)
    
    def run(self):
        """Exécute la boucle principale du jeu"""
        while self.running:
            self.running = self.handle_events()
            self.update()
            self.draw()
        
        # Sauvegarde des meilleurs scores avant de quitter
        self.save_high_scores()
