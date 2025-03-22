#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Générateur d'assets visuels
Génération des sprites pour le jeu
"""

from PIL import Image, ImageDraw
import os

def create_directory_if_not_exists(directory):
    """Crée un répertoire s'il n'existe pas
    
    Args:
        directory (str): Chemin du répertoire
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_player_sprite(output_path, size=32):
    """Génère le sprite du joueur (bateau pirate)
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 32.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleurs
    hull_color = (139, 69, 19)  # Marron
    sail_color = (255, 255, 255)  # Blanc
    flag_color = (0, 0, 0)  # Noir (drapeau pirate)
    
    # Dessin de la coque du bateau
    draw.ellipse([(size//4, size//2), (3*size//4, 7*size//8)], fill=hull_color)
    
    # Dessin du mât
    draw.rectangle([(size//2 - 1, size//8), (size//2 + 1, size//2)], fill=hull_color)
    
    # Dessin de la voile
    draw.polygon([(size//2, size//8), (3*size//4, size//4), (size//2, size//2)], fill=sail_color)
    
    # Dessin du drapeau pirate
    draw.rectangle([(size//2 - 1, size//8 - 5), (size//2 + 6, size//8)], fill=flag_color)
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite du joueur généré : {output_path}")

def generate_octopus_sprite(output_path, size=32):
    """Génère le sprite d'une pieuvre
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 32.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleur de la pieuvre
    octopus_color = (128, 0, 128)  # Violet
    
    # Dessin du corps de la pieuvre
    draw.ellipse([(size//4, size//4), (3*size//4, 3*size//4)], fill=octopus_color)
    
    # Dessin des tentacules
    # Tentacule 1
    draw.line([(size//4, size//2), (size//8, 3*size//4)], fill=octopus_color, width=2)
    # Tentacule 2
    draw.line([(size//3, 3*size//4), (size//4, 7*size//8)], fill=octopus_color, width=2)
    # Tentacule 3
    draw.line([(size//2, 3*size//4), (size//2, 7*size//8)], fill=octopus_color, width=2)
    # Tentacule 4
    draw.line([(2*size//3, 3*size//4), (3*size//4, 7*size//8)], fill=octopus_color, width=2)
    # Tentacule 5
    draw.line([(3*size//4, size//2), (7*size//8, 3*size//4)], fill=octopus_color, width=2)
    
    # Dessin des yeux
    draw.ellipse([(3*size//8, 3*size//8), (3*size//8 + 4, 3*size//8 + 4)], fill=(255, 255, 255))
    draw.ellipse([(5*size//8, 3*size//8), (5*size//8 + 4, 3*size//8 + 4)], fill=(255, 255, 255))
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite de pieuvre généré : {output_path}")

def generate_enemy_ship_sprite(output_path, size=32):
    """Génère le sprite d'un bateau ennemi
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 32.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleurs
    hull_color = (139, 0, 0)  # Rouge foncé
    sail_color = (220, 220, 220)  # Gris clair
    
    # Dessin de la coque du bateau
    draw.ellipse([(size//4, size//2), (3*size//4, 7*size//8)], fill=hull_color)
    
    # Dessin du mât
    draw.rectangle([(size//2 - 1, size//8), (size//2 + 1, size//2)], fill=hull_color)
    
    # Dessin de la voile
    draw.polygon([(size//2, size//8), (3*size//4, size//4), (size//2, size//2)], fill=sail_color)
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite de bateau ennemi généré : {output_path}")

def generate_wall_sprite(output_path, size=32):
    """Génère le sprite d'un mur (récif corallien)
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 32.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleur du récif
    reef_color = (0, 0, 139)  # Bleu foncé
    coral_color = (255, 127, 80)  # Corail
    
    # Dessin du fond marin
    draw.rectangle([(0, 0), (size, size)], fill=reef_color)
    
    # Dessin des coraux
    # Corail 1
    draw.ellipse([(size//8, size//8), (3*size//8, 3*size//8)], fill=coral_color)
    # Corail 2
    draw.ellipse([(5*size//8, size//4), (7*size//8, size//2)], fill=coral_color)
    # Corail 3
    draw.ellipse([(size//4, 5*size//8), (size//2, 7*size//8)], fill=coral_color)
    # Corail 4
    draw.ellipse([(5*size//8, 5*size//8), (3*size//4, 3*size//4)], fill=coral_color)
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite de mur généré : {output_path}")

def generate_point_sprite(output_path, size=8):
    """Génère le sprite d'un point (pièce d'or)
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 8.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleur de la pièce
    coin_color = (255, 215, 0)  # Or
    
    # Dessin de la pièce
    draw.ellipse([(0, 0), (size, size)], fill=coin_color)
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite de point généré : {output_path}")

def generate_power_point_sprite(output_path, size=16):
    """Génère le sprite d'un point de pouvoir (coffre au trésor)
    
    Args:
        output_path (str): Chemin de sortie
        size (int, optional): Taille du sprite. Defaults to 16.
    """
    # Création d'une nouvelle image avec canal alpha
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Couleurs
    chest_color = (139, 69, 19)  # Marron
    gold_color = (255, 215, 0)  # Or
    
    # Dessin du coffre
    draw.rectangle([(size//4, size//3), (3*size//4, 2*size//3)], fill=chest_color)
    
    # Dessin du couvercle
    draw.rectangle([(size//4, size//4), (3*size//4, size//3)], fill=chest_color)
    
    # Dessin de l'or qui dépasse
    draw.rectangle([(3*size//8, size//3), (5*size//8, 2*size//3)], fill=gold_color)
    
    # Sauvegarde de l'image
    image.save(output_path)
    print(f"Sprite de point de pouvoir généré : {output_path}")

def generate_all_sprites():
    """Génère tous les sprites nécessaires pour le jeu"""
    # Création des répertoires
    images_dir = os.path.join(os.getcwd(), "assets", "images")
    create_directory_if_not_exists(images_dir)
    
    # Génération des sprites
    generate_player_sprite(os.path.join(images_dir, "player.png"))
    generate_octopus_sprite(os.path.join(images_dir, "octopus.png"))
    generate_enemy_ship_sprite(os.path.join(images_dir, "enemy_ship.png"))
    generate_wall_sprite(os.path.join(images_dir, "wall.png"))
    generate_point_sprite(os.path.join(images_dir, "point.png"))
    generate_power_point_sprite(os.path.join(images_dir, "power_point.png"))

if __name__ == "__main__":
    generate_all_sprites()
