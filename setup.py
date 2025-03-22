#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script d'installation pour Pacman Pirate
Ce script vérifie et installe les dépendances nécessaires
"""

import sys
import subprocess
import os
import platform

def check_python_version():
    """Vérifie la version de Python"""
    print("Vérification de la version de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("ERREUR: Python 3.6 ou supérieur est requis")
        print(f"Version actuelle: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"Version de Python: {version.major}.{version.minor}.{version.micro} ✓")
    return True

def create_virtual_env():
    """Crée un environnement virtuel si nécessaire"""
    if os.path.exists("venv"):
        print("Environnement virtuel déjà existant ✓")
        return True
    
    print("Création d'un environnement virtuel...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Environnement virtuel créé avec succès ✓")
        return True
    except subprocess.CalledProcessError:
        print("ERREUR: Impossible de créer l'environnement virtuel")
        return False

def install_dependencies():
    """Installe les dépendances nécessaires"""
    print("Installation des dépendances...")
    
    # Déterminer le chemin de pip selon l'OS et l'environnement virtuel
    pip_cmd = "pip"
    if platform.system() == "Windows":
        pip_path = os.path.join("venv", "Scripts", "pip")
    else:
        pip_path = os.path.join("venv", "bin", "pip")
    
    if os.path.exists(pip_path):
        pip_cmd = pip_path
    
    try:
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("Dépendances installées avec succès ✓")
        return True
    except subprocess.CalledProcessError:
        print("ERREUR: Impossible d'installer les dépendances")
        return False

def print_activation_instructions():
    """Affiche les instructions d'activation de l'environnement virtuel"""
    print("\nPour activer l'environnement virtuel:")
    if platform.system() == "Windows":
        print("  venv\\Scripts\\activate")
    else:
        print("  source venv/bin/activate")

def print_run_instructions():
    """Affiche les instructions pour exécuter le jeu"""
    print("\nPour lancer le jeu:")
    print("  python main.py")

def main():
    """Fonction principale"""
    print("=== Installation de Pacman Pirate ===\n")
    
    if not check_python_version():
        return False
    
    if not create_virtual_env():
        return False
    
    if not install_dependencies():
        return False
    
    print("\n=== Installation terminée avec succès! ===")
    print_activation_instructions()
    print_run_instructions()
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
