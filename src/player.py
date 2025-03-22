#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module Player
Gestion du joueur (bateau pirate)
"""

import pygame

class Player:
    """Classe représentant le joueur (bateau pirate)"""
    
    def __init__(self, x, y, speed=5):
        """Initialisation du joueur
        
        Args:
            x (int): Position initiale x
            y (int): Position initiale y
            speed (int): Vitesse de déplacement
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = "right"  # Direction initiale
        self.lives = 3
        self.score = 0
        self.image = None  # Sera chargé plus tard
        self.rect = pygame.Rect(x, y, 32, 32)  # Rectangle de collision temporaire
    
    def load_image(self, image_path):
        """Charge l'image du joueur
        
        Args:
            image_path (str): Chemin vers l'image
        """
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        except pygame.error as e:
            print(f"Impossible de charger l'image du joueur: {e}")
            # Utiliser un rectangle coloré par défaut
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 255, 0))  # Jaune
    
    def update(self, keys, maze):
        """Met à jour la position du joueur en fonction des touches pressées
        
        Args:
            keys (dict): État des touches du clavier
            maze (Maze): Labyrinthe pour la détection des collisions
        """
        # Sauvegarde de la position actuelle pour pouvoir revenir en arrière en cas de collision
        old_x, old_y = self.x, self.y
        
        # Déplacement en fonction des touches
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = "right"
        elif keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = "down"
        
        # Mise à jour du rectangle de collision
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Détection des collisions avec les murs (à implémenter quand la classe Maze sera prête)
        if maze and self.check_collision(maze):
            # Retour à la position précédente en cas de collision
            self.x, self.y = old_x, old_y
            self.rect.x = self.x
            self.rect.y = self.y
    
    def check_collision(self, maze):
        """Vérifie les collisions avec les murs du labyrinthe
        
        Args:
            maze (Maze): Labyrinthe pour la détection des collisions
            
        Returns:
            bool: True si collision, False sinon
        """
        # Utiliser la méthode check_collision de la classe Maze
        return maze.check_collision(self.rect)
    
    def collect_point(self, points):
        """Collecte des points et met à jour le score
        
        Args:
            points (int): Nombre de points à ajouter
        """
        self.score += points
    
    def lose_life(self):
        """Perd une vie et vérifie si le jeu est terminé
        
        Returns:
            bool: True si le joueur est toujours en vie, False sinon
        """
        self.lives -= 1
        return self.lives > 0
    
    def draw(self, screen):
        """Dessine le joueur sur l'écran
        
        Args:
            screen (Surface): Surface d'affichage
        """
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Dessiner un rectangle par défaut si l'image n'est pas chargée
            pygame.draw.rect(screen, (255, 255, 0), self.rect)
