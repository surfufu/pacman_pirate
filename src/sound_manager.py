#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pacman Pirate - Gestionnaire de sons
Création de placeholders pour les effets sonores
"""

import os
import pygame

def create_directory_if_not_exists(directory):
    """Crée un répertoire s'il n'existe pas
    
    Args:
        directory (str): Chemin du répertoire
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

class SoundManager:
    """Classe gérant les sons du jeu"""
    
    def __init__(self):
        """Initialisation du gestionnaire de sons"""
        self.sounds = {}
        self.music_playing = False
        
        # Vérification que pygame.mixer est initialisé
        if not pygame.mixer.get_init():
            pygame.mixer.init()
    
    def create_placeholder_sounds(self, sounds_dir):
        """Crée des placeholders pour les sons
        
        Args:
            sounds_dir (str): Répertoire des sons
        """
        # Création du répertoire des sons
        create_directory_if_not_exists(sounds_dir)
        
        # Liste des sons à créer
        sound_files = {
            "move": "move.wav",
            "collect": "collect.wav",
            "power": "power.wav",
            "hit": "hit.wav",
            "game_over": "game_over.wav",
            "victory": "victory.wav",
            "menu": "menu.wav"
        }
        
        # Création d'un fichier texte expliquant les placeholders
        placeholder_info = """
Placeholders pour les sons du jeu Pacman Pirate

Ces fichiers sont des placeholders pour les sons du jeu.
Vous pouvez les remplacer par vos propres fichiers audio.

Liste des sons:
- move.wav: Son de déplacement du joueur
- collect.wav: Son de collecte des points
- power.wav: Son de collecte des points de pouvoir
- hit.wav: Son de collision avec un ennemi
- game_over.wav: Son de fin de partie
- victory.wav: Son de victoire
- menu.wav: Musique du menu
- background.wav: Musique de fond pendant le jeu

Formats recommandés: WAV ou OGG
"""
        with open(os.path.join(sounds_dir, "README.txt"), "w") as f:
            f.write(placeholder_info)
        
        print(f"Fichier d'information sur les placeholders créé : {os.path.join(sounds_dir, 'README.txt')}")
        
        # Création d'un fichier texte pour chaque son
        for sound_name, sound_file in sound_files.items():
            with open(os.path.join(sounds_dir, sound_file), "w") as f:
                f.write(f"Placeholder pour le son {sound_name}")
            print(f"Placeholder pour le son {sound_name} créé : {os.path.join(sounds_dir, sound_file)}")
        
        # Création d'un placeholder pour la musique de fond
        with open(os.path.join(sounds_dir, "background.wav"), "w") as f:
            f.write("Placeholder pour la musique de fond")
        print(f"Placeholder pour la musique de fond créé : {os.path.join(sounds_dir, 'background.wav')}")
    
    def load_sounds(self, sounds_dir):
        """Charge les sons du jeu
        
        Args:
            sounds_dir (str): Répertoire des sons
        """
        # Liste des sons à charger
        sound_files = {
            "move": "move.wav",
            "collect": "collect.wav",
            "power": "power.wav",
            "hit": "hit.wav",
            "game_over": "game_over.wav",
            "victory": "victory.wav",
            "menu": "menu.wav"
        }
        
        # Chargement des sons
        for sound_name, sound_file in sound_files.items():
            sound_path = os.path.join(sounds_dir, sound_file)
            try:
                if os.path.getsize(sound_path) > 100:  # Vérifier que ce n'est pas un placeholder texte
                    self.sounds[sound_name] = pygame.mixer.Sound(sound_path)
                    print(f"Son {sound_name} chargé : {sound_path}")
                else:
                    print(f"Son {sound_name} est un placeholder, il ne sera pas chargé")
            except (pygame.error, FileNotFoundError) as e:
                print(f"Impossible de charger le son {sound_name}: {e}")
    
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
            if os.path.getsize(music_path) > 100:  # Vérifier que ce n'est pas un placeholder texte
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(loops)
                self.music_playing = True
                print(f"Musique chargée : {music_path}")
            else:
                print(f"Musique {music_path} est un placeholder, elle ne sera pas chargée")
        except (pygame.error, FileNotFoundError) as e:
            print(f"Impossible de charger la musique: {e}")
            self.music_playing = False
    
    def stop_music(self):
        """Arrête la musique de fond"""
        pygame.mixer.music.stop()
        self.music_playing = False

def create_sound_placeholders():
    """Crée des placeholders pour les sons du jeu"""
    # Création du gestionnaire de sons
    sound_manager = SoundManager()
    
    # Création des placeholders
    sounds_dir = os.path.join(os.getcwd(), "assets", "sounds")
    sound_manager.create_placeholder_sounds(sounds_dir)

if __name__ == "__main__":
    # Création des placeholders sans initialiser pygame.mixer
    # (pour éviter les erreurs dans les environnements sans périphérique audio)
    try:
        pygame.init()
        print("Création des placeholders pour les sons...")
        create_sound_placeholders()
    except Exception as e:
        print(f"Erreur lors de l'initialisation de pygame: {e}")
        # Création manuelle des répertoires et fichiers
        sounds_dir = os.path.join(os.getcwd(), "assets", "sounds")
        create_directory_if_not_exists(sounds_dir)
        
        # Création d'un fichier texte expliquant les placeholders
        placeholder_info = """
Placeholders pour les sons du jeu Pacman Pirate

Ces fichiers sont des placeholders pour les sons du jeu.
Vous pouvez les remplacer par vos propres fichiers audio.

Liste des sons:
- move.wav: Son de déplacement du joueur
- collect.wav: Son de collecte des points
- power.wav: Son de collecte des points de pouvoir
- hit.wav: Son de collision avec un ennemi
- game_over.wav: Son de fin de partie
- victory.wav: Son de victoire
- menu.wav: Musique du menu
- background.wav: Musique de fond pendant le jeu

Formats recommandés: WAV ou OGG
"""
        with open(os.path.join(sounds_dir, "README.txt"), "w") as f:
            f.write(placeholder_info)
        
        print(f"Fichier d'information sur les placeholders créé : {os.path.join(sounds_dir, 'README.txt')}")
        
        # Liste des sons à créer
        sound_files = {
            "move": "move.wav",
            "collect": "collect.wav",
            "power": "power.wav",
            "hit": "hit.wav",
            "game_over": "game_over.wav",
            "victory": "victory.wav",
            "menu": "menu.wav",
            "background": "background.wav"
        }
        
        # Création d'un fichier texte pour chaque son
        for sound_name, sound_file in sound_files.items():
            with open(os.path.join(sounds_dir, sound_file), "w") as f:
                f.write(f"Placeholder pour le son {sound_name}")
            print(f"Placeholder pour le son {sound_name} créé : {os.path.join(sounds_dir, sound_file)}")
    
    print("Création des placeholders terminée.")
