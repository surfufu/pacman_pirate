#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module Enemy
Gestion des ennemis (pieuvres et bateaux ennemis)
"""

import pygame
import random

class Enemy:
    """Classe de base pour les ennemis"""
    
    def __init__(self, x, y, speed=3):
        """Initialisation de l'ennemi
        
        Args:
            x (int): Position initiale x
            y (int): Position initiale y
            speed (int): Vitesse de déplacement
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])
        self.image = None  # Sera chargé plus tard
        self.rect = pygame.Rect(x, y, 32, 32)  # Rectangle de collision temporaire
    
    def load_image(self, image_path):
        """Charge l'image de l'ennemi
        
        Args:
            image_path (str): Chemin vers l'image
        """
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
        except pygame.error as e:
            print(f"Impossible de charger l'image de l'ennemi: {e}")
            # Utiliser un rectangle coloré par défaut
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 0, 0))  # Rouge
    
    def update(self, maze):
        """Met à jour la position de l'ennemi
        
        Args:
            maze (Maze): Labyrinthe pour la détection des collisions
        """
        # Sauvegarde de la position actuelle pour pouvoir revenir en arrière en cas de collision
        old_x, old_y = self.x, self.y
        
        # Déplacement en fonction de la direction
        if self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        
        # Mise à jour du rectangle de collision
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Détection des collisions avec les murs (à implémenter quand la classe Maze sera prête)
        if maze and self.check_collision(maze):
            # Retour à la position précédente en cas de collision
            self.x, self.y = old_x, old_y
            self.rect.x = self.x
            self.rect.y = self.y
            # Changement de direction aléatoire
            self.change_direction()
    
    def check_collision(self, maze):
        """Vérifie les collisions avec les murs du labyrinthe
        
        Args:
            maze (Maze): Labyrinthe pour la détection des collisions
            
        Returns:
            bool: True si collision, False sinon
        """
        # Utiliser la méthode check_collision de la classe Maze
        return maze.check_collision(self.rect)
    
    def change_direction(self):
        """Change la direction de l'ennemi aléatoirement"""
        directions = ["up", "down", "left", "right"]
        # Éviter de choisir la même direction
        directions.remove(self.direction)
        self.direction = random.choice(directions)
    
    def check_player_collision(self, player):
        """Vérifie si l'ennemi est en collision avec le joueur
        
        Args:
            player (Player): Joueur à vérifier
            
        Returns:
            bool: True si collision, False sinon
        """
        return self.rect.colliderect(player.rect)
    
    def draw(self, screen):
        """Dessine l'ennemi sur l'écran
        
        Args:
            screen (Surface): Surface d'affichage
        """
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            # Dessiner un rectangle par défaut si l'image n'est pas chargée
            pygame.draw.rect(screen, (255, 0, 0), self.rect)


class Octopus(Enemy):
    """Classe pour les ennemis de type pieuvre"""
    
    def __init__(self, x, y, speed=2):
        """Initialisation de la pieuvre
        
        Args:
            x (int): Position initiale x
            y (int): Position initiale y
            speed (int): Vitesse de déplacement
        """
        super().__init__(x, y, speed)
        self.color = (128, 0, 128)  # Violet
    
    def update(self, maze, player=None):
        """Met à jour la position de la pieuvre avec un mouvement plus aléatoire
        
        Args:
            maze (Maze): Labyrinthe pour la détection des collisions
            player (Player, optional): Joueur pour le suivi. Defaults to None.
        """
        # Changement aléatoire de direction (10% de chance)
        if random.random() < 0.1:
            self.change_direction()
        
        super().update(maze)


class EnemyShip(Enemy):
    """Classe pour les ennemis de type bateau ennemi"""
    
    def __init__(self, x, y, speed=3):
        """Initialisation du bateau ennemi
        
        Args:
            x (int): Position initiale x
            y (int): Position initiale y
            speed (int): Vitesse de déplacement
        """
        super().__init__(x, y, speed)
        self.color = (255, 0, 0)  # Rouge
    
    def update(self, maze, player=None):
        """Met à jour la position du bateau ennemi avec un suivi basique du joueur
        
        Args:
            maze (Maze): Labyrinthe pour la détection des collisions
            player (Player, optional): Joueur à suivre. Defaults to None.
        """
        # Si le joueur est fourni et qu'on a 30% de chance, on essaie de le suivre
        if player and random.random() < 0.3:
            # Déterminer la direction vers le joueur
            dx = player.x - self.x
            dy = player.y - self.y
            
            if abs(dx) > abs(dy):
                # Mouvement horizontal prioritaire
                self.direction = "right" if dx > 0 else "left"
            else:
                # Mouvement vertical prioritaire
                self.direction = "down" if dy > 0 else "up"
        
        super().update(maze)
