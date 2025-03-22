#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Module de niveaux
Définition des niveaux du jeu
"""

class LevelManager:
    """Classe gérant les niveaux du jeu"""
    
    def __init__(self):
        """Initialisation du gestionnaire de niveaux"""
        self.levels = {}
        self.init_levels()
    
    def init_levels(self):
        """Initialise les niveaux du jeu"""
        # Niveau 1 - Facile
        self.levels[1] = {
            "name": "Mer des Caraïbes",
            "layout": [
                "####################",
                "#........#.........#",
                "#.######.#.######.#",
                "#.#....#.#.#....#.#",
                "#.#.##.#.#.#.##.#.#",
                "#.#.#o.....#.#o.#.#",
                "#...#.#####.#...#.#",
                "###.#.#...#.#.###.#",
                "#...#.#.#.#.#.....#",
                "#.###.#.#.#.#####.#",
                "#.....#.#.#.......#",
                "#.#####.#.#########",
                "#.#.....#.........#",
                "#.#.#############.#",
                "#.#.#.........#.#.#",
                "#.#.#.#######.#.#.#",
                "#.#.#.#.....#.#.#.#",
                "#...#...###...#...#",
                "################.##",
                "P..................#",
                "####################"
            ],
            "player_start": (1, 19),  # Position de départ du joueur (x, y)
            "enemies": [
                {"type": "octopus", "position": (10, 10)},
                {"type": "octopus", "position": (15, 5)},
                {"type": "octopus", "position": (5, 15)},
                {"type": "ship", "position": (18, 3)}
            ],
            "speed_multiplier": 1.0  # Multiplicateur de vitesse (normal)
        }
        
        # Niveau 2 - Moyen
        self.levels[2] = {
            "name": "Détroit de Gibraltar",
            "layout": [
                "####################",
                "#o.................#",
                "#.##############.##",
                "#.#............#..#",
                "#.#.##########.#.##",
                "#.#.#........#.#..#",
                "#.#.#.######.#.##.#",
                "#.#.#.#....#.#....#",
                "#.#.#.#.##.#.#.####",
                "#...#...##...#....#",
                "###.###.#########.#",
                "#...#...#.........#",
                "#.###.###.#########",
                "#.....#...#.......#",
                "#####.#.###.#####.#",
                "#.....#.#...#...#.#",
                "#.#####.#.###.#.#.#",
                "#.......#.....#...#",
                "##############.####",
                "P..................#",
                "####################"
            ],
            "player_start": (1, 19),
            "enemies": [
                {"type": "octopus", "position": (10, 5)},
                {"type": "octopus", "position": (15, 10)},
                {"type": "ship", "position": (5, 15)}
            ],
            "speed_multiplier": 1.2  # Légèrement plus rapide
        }
        
        # Niveau 3 - Difficile
        self.levels[3] = {
            "name": "Triangle des Bermudes",
            "layout": [
                "####################",
                "#o.................#",
                "#.##############.##",
                "#.#............#..#",
                "#.#.##########.#.##",
                "#.#.#........#.#..#",
                "#.#.#.######.#.##.#",
                "#.#.#.#....#.#....#",
                "#.#.#.#.##.#.#.####",
                "#...#...##...#....#",
                "###.###.#########.#",
                "#...#...#.........#",
                "#.###.###.#########",
                "#.....#...#.......#",
                "#####.#.###.#####.#",
                "#.....#.#...#...#.#",
                "#.#####.#.###.#.#.#",
                "#.......#.....#...#",
                "##############.####",
                "P..................#",
                "####################"
            ],
            "player_start": (1, 19),
            "enemies": [
                {"type": "octopus", "position": (10, 5)},
                {"type": "octopus", "position": (15, 10)},
                {"type": "ship", "position": (5, 15)},
                {"type": "ship", "position": (18, 3)}
            ],
            "speed_multiplier": 1.5  # Beaucoup plus rapide
        }
    
    def get_level(self, level_number):
        """Récupère les données d'un niveau
        
        Args:
            level_number (int): Numéro du niveau
            
        Returns:
            dict: Données du niveau ou None si le niveau n'existe pas
        """
        return self.levels.get(level_number)
    
    def get_max_level(self):
        """Récupère le numéro du niveau maximum
        
        Returns:
            int: Numéro du niveau maximum
        """
        return max(self.levels.keys())
    
    def parse_layout(self, layout):
        """Analyse la disposition du niveau
        
        Args:
            layout (list): Liste de chaînes représentant le niveau
            
        Returns:
            tuple: (walls, points, power_points, player_start, enemy_positions)
        """
        walls = []
        points = []
        power_points = []
        player_start = None
        
        for y, row in enumerate(layout):
            for x, cell in enumerate(row):
                if cell == '#':
                    walls.append((x, y))
                elif cell == '.':
                    points.append((x, y))
                elif cell == 'o':
                    power_points.append((x, y))
                elif cell == 'P':
                    player_start = (x, y)
        
        return walls, points, power_points, player_start
