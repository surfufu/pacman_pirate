#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module de menus améliorés
Implémentation des menus et des transitions entre niveaux
"""

import pygame
import sys
import os

class MenuManager:
    """Classe gérant les menus du jeu"""
    
    def __init__(self, screen, sound_manager=None):
        """Initialisation du gestionnaire de menus
        
        Args:
            screen (Surface): Surface d'affichage
            sound_manager (SoundManager, optional): Gestionnaire de sons. Defaults to None.
        """
        self.screen = screen
        self.sound_manager = sound_manager
        
        # Polices
        self.font_title = pygame.font.SysFont(None, 72)
        self.font_large = pygame.font.SysFont(None, 48)
        self.font_medium = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 24)
        
        # Couleurs
        self.color_title = (255, 215, 0)  # Or
        self.color_text = (255, 255, 255)  # Blanc
        self.color_highlight = (255, 165, 0)  # Orange
        self.color_background = (0, 0, 128)  # Bleu foncé
        
        # Animation
        self.animation_counter = 0
        self.animation_speed = 0.1
    
    def draw_main_menu(self, high_scores=None):
        """Dessine le menu principal
        
        Args:
            high_scores (list, optional): Liste des meilleurs scores. Defaults to None.
        """
        # Effacement de l'écran
        self.screen.fill(self.color_background)
        
        # Animation du titre
        self.animation_counter += self.animation_speed
        title_offset = int(5 * abs(pygame.math.sin(self.animation_counter)))
        
        # Titre
        text_title = self.font_title.render("Pacman Pirate", True, self.color_title)
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 150 + title_offset))
        self.screen.blit(text_title, text_rect_title)
        
        # Sous-titre
        text_subtitle = self.font_medium.render("Une aventure en haute mer", True, self.color_text)
        text_rect_subtitle = text_subtitle.get_rect(center=(self.screen.get_width() // 2, 220))
        self.screen.blit(text_subtitle, text_rect_subtitle)
        
        # Options du menu
        # Jouer
        text_play = self.font_medium.render("Appuyez sur ESPACE pour jouer", True, self.color_text)
        text_rect_play = text_play.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_play, text_rect_play)
        
        # Instructions
        text_instructions = self.font_medium.render("Utilisez les flèches pour déplacer votre bateau", True, self.color_text)
        text_rect_instructions = text_instructions.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(text_instructions, text_rect_instructions)
        
        # Quitter
        text_quit = self.font_medium.render("Appuyez sur ÉCHAP pour quitter", True, self.color_text)
        text_rect_quit = text_quit.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(text_quit, text_rect_quit)
        
        # Meilleurs scores
        if high_scores:
            text_scores = self.font_medium.render("Meilleurs scores:", True, self.color_text)
            text_rect_scores = text_scores.get_rect(center=(self.screen.get_width() // 2, 480))
            self.screen.blit(text_scores, text_rect_scores)
            
            for i, score in enumerate(high_scores[:5]):
                text_score = self.font_small.render(f"{i+1}. {score}", True, self.color_text)
                text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 520 + i * 30))
                self.screen.blit(text_score, text_rect_score)
        
        # Crédits
        text_credits = self.font_small.render("Développé avec Pygame", True, self.color_text)
        text_rect_credits = text_credits.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 30))
        self.screen.blit(text_credits, text_rect_credits)
    
    def draw_pause_menu(self):
        """Dessine le menu de pause"""
        # Fond semi-transparent
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Noir semi-transparent
        self.screen.blit(overlay, (0, 0))
        
        # Titre
        text_title = self.font_large.render("Pause", True, self.color_title)
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(text_title, text_rect_title)
        
        # Options
        text_resume = self.font_medium.render("Appuyez sur ESPACE pour continuer", True, self.color_text)
        text_rect_resume = text_resume.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_resume, text_rect_resume)
        
        text_menu = self.font_medium.render("Appuyez sur M pour retourner au menu", True, self.color_text)
        text_rect_menu = text_menu.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(text_menu, text_rect_menu)
        
        text_quit = self.font_medium.render("Appuyez sur ÉCHAP pour quitter", True, self.color_text)
        text_rect_quit = text_quit.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(text_quit, text_rect_quit)
    
    def draw_level_transition(self, level_number, level_name):
        """Dessine la transition entre les niveaux
        
        Args:
            level_number (int): Numéro du niveau
            level_name (str): Nom du niveau
        """
        # Effacement de l'écran
        self.screen.fill(self.color_background)
        
        # Titre
        text_title = self.font_large.render(f"Niveau {level_number}", True, self.color_title)
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(text_title, text_rect_title)
        
        # Nom du niveau
        text_name = self.font_medium.render(level_name, True, self.color_text)
        text_rect_name = text_name.get_rect(center=(self.screen.get_width() // 2, 270))
        self.screen.blit(text_name, text_rect_name)
        
        # Instructions
        text_instructions = self.font_medium.render("Préparez-vous à naviguer !", True, self.color_text)
        text_rect_instructions = text_instructions.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(text_instructions, text_rect_instructions)
        
        # Continuer
        text_continue = self.font_medium.render("Appuyez sur ESPACE pour commencer", True, self.color_text)
        text_rect_continue = text_continue.get_rect(center=(self.screen.get_width() // 2, 450))
        self.screen.blit(text_continue, text_rect_continue)
    
    def draw_game_over(self, score):
        """Dessine l'écran de game over
        
        Args:
            score (int): Score final
        """
        # Effacement de l'écran
        self.screen.fill(self.color_background)
        
        # Animation du titre
        self.animation_counter += self.animation_speed
        title_offset = int(5 * abs(pygame.math.sin(self.animation_counter)))
        
        # Titre
        text_title = self.font_title.render("Game Over", True, (255, 0, 0))  # Rouge
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200 + title_offset))
        self.screen.blit(text_title, text_rect_title)
        
        # Score
        text_score = self.font_large.render(f"Score: {score}", True, self.color_text)
        text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_score, text_rect_score)
        
        # Message
        text_message = self.font_medium.render("Votre navire a coulé !", True, self.color_text)
        text_rect_message = text_message.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(text_message, text_rect_message)
        
        # Rejouer
        text_play = self.font_medium.render("Appuyez sur ESPACE pour rejouer", True, self.color_text)
        text_rect_play = text_play.get_rect(center=(self.screen.get_width() // 2, 420))
        self.screen.blit(text_play, text_rect_play)
        
        # Menu
        text_menu = self.font_medium.render("Appuyez sur M pour retourner au menu", True, self.color_text)
        text_rect_menu = text_menu.get_rect(center=(self.screen.get_width() // 2, 470))
        self.screen.blit(text_menu, text_rect_menu)
    
    def draw_victory(self, score, is_final_level):
        """Dessine l'écran de victoire
        
        Args:
            score (int): Score final
            is_final_level (bool): True si c'est le dernier niveau
        """
        # Effacement de l'écran
        self.screen.fill(self.color_background)
        
        # Animation du titre
        self.animation_counter += self.animation_speed
        title_offset = int(5 * abs(pygame.math.sin(self.animation_counter)))
        
        # Titre
        text_title = self.font_title.render("Victoire !", True, (0, 255, 0))  # Vert
        text_rect_title = text_title.get_rect(center=(self.screen.get_width() // 2, 200 + title_offset))
        self.screen.blit(text_title, text_rect_title)
        
        # Score
        text_score = self.font_large.render(f"Score: {score}", True, self.color_text)
        text_rect_score = text_score.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_score, text_rect_score)
        
        # Message
        if is_final_level:
            text_message = self.font_medium.render("Félicitations ! Vous avez terminé le jeu !", True, self.color_text)
            text_rect_message = text_message.get_rect(center=(self.screen.get_width() // 2, 350))
            self.screen.blit(text_message, text_rect_message)
            
            text_next = self.font_medium.render("Vous êtes un véritable pirate !", True, self.color_text)
            text_rect_next = text_next.get_rect(center=(self.screen.get_width() // 2, 400))
            self.screen.blit(text_next, text_rect_next)
        else:
            text_message = self.font_medium.render("Niveau terminé !", True, self.color_text)
            text_rect_message = text_message.get_rect(center=(self.screen.get_width() // 2, 350))
            self.screen.blit(text_message, text_rect_message)
            
            text_next = self.font_medium.render("Appuyez sur ESPACE pour le niveau suivant", True, self.color_text)
            text_rect_next = text_next.get_rect(center=(self.screen.get_width() // 2, 400))
            self.screen.blit(text_next, text_rect_next)
        
        # Menu
        text_menu = self.font_medium.render("Appuyez sur M pour retourner au menu", True, self.color_text)
        text_rect_menu = text_menu.get_rect(center=(self.screen.get_width() // 2, 470))
        self.screen.blit(text_menu, text_rect_menu)
    
    def draw_loading(self):
        """Dessine un écran de chargement"""
        # Effacement de l'écran
        self.screen.fill(self.color_background)
        
        # Animation
        self.animation_counter += self.animation_speed
        dots = "." * (1 + int(self.animation_counter) % 3)
        
        # Message
        text_loading = self.font_large.render(f"Chargement{dots}", True, self.color_text)
        text_rect_loading = text_loading.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_loading, text_rect_loading)
        
        # Rafraîchissement de l'écran
        pygame.display.flip()
    
    def play_menu_sound(self, sound_name):
        """Joue un son de menu
        
        Args:
            sound_name (str): Nom du son à jouer
        """
        if self.sound_manager:
            self.sound_manager.play_sound(sound_name)
