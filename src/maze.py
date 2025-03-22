#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module Maze
Gestion du labyrinthe océanique
"""

import pygame

class Maze:
    """Classe représentant le labyrinthe océanique"""
    
    def __init__(self, width, height, cell_size):
        """Initialisation du labyrinthe
        
        Args:
            width (int): Largeur du labyrinthe en nombre de cellules
            height (int): Hauteur du labyrinthe en nombre de cellules
            cell_size (int): Taille d'une cellule en pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = []
        self.walls = []
        self.points = []
        self.power_points = []
        self.wall_image = None
        
        # Initialisation de la grille vide
        self.init_empty_grid()
    
    def init_empty_grid(self):
        """Initialise une grille vide"""
        # 0 = chemin, 1 = mur, 2 = point, 3 = point de pouvoir
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def load_level(self, level_data):
        """Charge un niveau à partir de données
        
        Args:
            level_data (list): Données du niveau sous forme de liste de chaînes
        """
        self.init_empty_grid()
        
        for y, row in enumerate(level_data):
            for x, cell in enumerate(row):
                if x < self.width and y < self.height:
                    if cell == '#':  # Mur
                        self.grid[y][x] = 1
                        self.walls.append(pygame.Rect(x * self.cell_size, y * self.cell_size, 
                                                     self.cell_size, self.cell_size))
                    elif cell == '.':  # Point
                        self.grid[y][x] = 2
                        self.points.append(pygame.Rect(x * self.cell_size + self.cell_size//2 - 2, 
                                                      y * self.cell_size + self.cell_size//2 - 2, 
                                                      4, 4))
                    elif cell == 'o':  # Point de pouvoir
                        self.grid[y][x] = 3
                        self.power_points.append(pygame.Rect(x * self.cell_size + self.cell_size//2 - 5, 
                                                           y * self.cell_size + self.cell_size//2 - 5, 
                                                           10, 10))
    
    def load_wall_image(self, image_path):
        """Charge l'image des murs
        
        Args:
            image_path (str): Chemin vers l'image
        """
        try:
            self.wall_image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Impossible de charger l'image du mur: {e}")
            self.wall_image = None
    
    def is_wall(self, x, y):
        """Vérifie si la position donnée contient un mur
        
        Args:
            x (int): Position x en pixels
            y (int): Position y en pixels
            
        Returns:
            bool: True si c'est un mur, False sinon
        """
        # Conversion des coordonnées en pixels vers les indices de la grille
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size
        
        # Vérification des limites
        if grid_x < 0 or grid_x >= self.width or grid_y < 0 or grid_y >= self.height:
            return True  # Considérer les bords comme des murs
        
        return self.grid[grid_y][grid_x] == 1
    
    def check_collision(self, rect):
        """Vérifie si un rectangle est en collision avec un mur
        
        Args:
            rect (Rect): Rectangle à vérifier
            
        Returns:
            bool: True si collision, False sinon
        """
        # Créer un rectangle légèrement plus petit pour la détection
        # Cela permet d'éviter les blocages aux bords
        tolerance = 2  # Pixels de tolérance
        check_rect = pygame.Rect(
            rect.x + tolerance,
            rect.y + tolerance,
            rect.width - 2 * tolerance,
            rect.height - 2 * tolerance
        )
        
        for wall in self.walls:
            if check_rect.colliderect(wall):
                return True
        return False
    
    def collect_point(self, rect):
        """Vérifie si un rectangle collecte un point et le supprime si c'est le cas
        
        Args:
            rect (Rect): Rectangle à vérifier
            
        Returns:
            int: Points gagnés (1 pour un point normal, 10 pour un point de pouvoir, 0 sinon)
        """
        # Vérifier les points normaux
        for i, point in enumerate(self.points):
            if rect.colliderect(point):
                del self.points[i]
                # Mettre à jour la grille
                grid_x = point.x // self.cell_size
                grid_y = point.y // self.cell_size
                if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
                    self.grid[grid_y][grid_x] = 0
                return 1
        
        # Vérifier les points de pouvoir
        for i, power_point in enumerate(self.power_points):
            if rect.colliderect(power_point):
                del self.power_points[i]
                # Mettre à jour la grille
                grid_x = power_point.x // self.cell_size
                grid_y = power_point.y // self.cell_size
                if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
                    self.grid[grid_y][grid_x] = 0
                return 10
        
        return 0
    
    def draw(self, screen):
        """Dessine le labyrinthe sur l'écran
        
        Args:
            screen (Surface): Surface d'affichage
        """
        # Dessiner les murs
        for wall in self.walls:
            if self.wall_image:
                screen.blit(self.wall_image, wall)
            else:
                pygame.draw.rect(screen, (0, 0, 139), wall)  # Bleu foncé
        
        # Dessiner les points
        for point in self.points:
            pygame.draw.rect(screen, (255, 215, 0), point)  # Or
        
        # Dessiner les points de pouvoir
        for power_point in self.power_points:
            pygame.draw.rect(screen, (255, 255, 255), power_point)  # Blanc
    
    def is_complete(self):
        """Vérifie si tous les points ont été collectés
        
        Returns:
            bool: True si tous les points ont été collectés, False sinon
        """
        return len(self.points) == 0 and len(self.power_points) == 0
