# Documentation du Projet Pacman Pirate

## Vue d'ensemble

Pacman Pirate est un jeu inspiré de Pacman, mais sur un thème pirate. Le joueur incarne un bateau pirate qui doit parcourir un labyrinthe océanique, collecter des points (pièces d'or) et éviter ou combattre des ennemis tels que des pieuvres et des bateaux ennemis.

Le jeu est développé en Python en utilisant la bibliothèque Pygame. Il comprend plusieurs niveaux de difficulté, un système de score, et des effets visuels et sonores.

## Structure du projet

Le projet est organisé selon la structure suivante :

```
pacman_pirate/
├── assets/
│   ├── images/
│   │   ├── player.png
│   │   ├── octopus.png
│   │   ├── enemy_ship.png
│   │   ├── wall.png
│   │   ├── point.png
│   │   └── power_point.png
│   └── sounds/
│       ├── move.wav
│       ├── collect.wav
│       ├── power.wav
│       ├── hit.wav
│       ├── game_over.wav
│       ├── victory.wav
│       ├── menu.wav
│       ├── background.wav
│       └── README.txt
├── src/
│   ├── player.py
│   ├── enemy.py
│   ├── maze.py
│   ├── game_manager.py
│   ├── level_manager.py
│   ├── sound_manager.py
│   ├── menu_manager.py
│   ├── maze_integration.py
│   ├── player_integration.py
│   ├── enemy_integration.py
│   ├── asset_generator.py
│   ├── game.py
│   └── test_game.py
├── main.py
└── todo.md
```

## Modules principaux

### main.py

Point d'entrée du jeu. Initialise et lance le jeu.

### src/game.py

Contient la classe principale `PacmanPirate` qui gère la boucle de jeu, les états du jeu, et l'intégration de tous les composants.

### src/player.py

Définit la classe `Player` qui représente le bateau pirate contrôlé par le joueur. Gère le mouvement, les collisions et la collecte des points.

### src/enemy.py

Définit les classes `Enemy`, `Octopus` et `EnemyShip` qui représentent les ennemis. Gère leur mouvement et leur comportement.

### src/maze.py

Définit la classe `Maze` qui représente le labyrinthe océanique. Gère la structure du labyrinthe, les murs, les points et les collisions.

### src/game_manager.py

Définit la classe `GameManager` qui gère l'état global du jeu, les scores et les niveaux.

### src/level_manager.py

Définit la classe `LevelManager` qui gère les différents niveaux du jeu et leur chargement.

### src/sound_manager.py

Définit la classe `SoundManager` qui gère les effets sonores et la musique du jeu.

### src/menu_manager.py

Définit la classe `MenuManager` qui gère les différents menus et écrans du jeu.

### src/asset_generator.py

Génère les sprites pour le jeu en utilisant la bibliothèque Pillow.

### src/test_game.py

Contient des tests pour vérifier le bon fonctionnement du jeu.

## Classes principales

### PacmanPirate

Classe principale du jeu qui gère la boucle de jeu, les états du jeu, et l'intégration de tous les composants.

#### Attributs principaux

- `width`, `height` : Dimensions de la fenêtre de jeu
- `fps` : Images par seconde
- `cell_size` : Taille d'une cellule du labyrinthe
- `screen` : Surface d'affichage Pygame
- `clock` : Horloge Pygame pour contrôler la vitesse du jeu
- `level_manager`, `game_manager`, `sound_manager`, `menu_manager` : Gestionnaires du jeu
- `player` : Instance du joueur
- `enemies` : Liste des ennemis
- `maze` : Instance du labyrinthe
- `game_state` : État actuel du jeu (menu, playing, pause, level_transition, game_over, victory)
- `current_level` : Niveau actuel
- `score` : Score du joueur
- `lives` : Vies restantes du joueur

#### Méthodes principales

- `load_assets()` : Charge les images et les sons
- `initialize_level(level_number)` : Initialise un niveau
- `handle_events()` : Gère les événements du jeu
- `update()` : Met à jour l'état du jeu
- `draw()` : Dessine les éléments du jeu
- `start_game()` : Démarre une nouvelle partie
- `run()` : Exécute la boucle principale du jeu

### Player

Représente le bateau pirate contrôlé par le joueur.

#### Attributs principaux

- `x`, `y` : Position du joueur
- `speed` : Vitesse de déplacement
- `direction` : Direction actuelle
- `lives` : Nombre de vies
- `score` : Score du joueur
- `image` : Image du joueur
- `rect` : Rectangle de collision

#### Méthodes principales

- `load_image(image_path)` : Charge l'image du joueur
- `update(keys, maze)` : Met à jour la position du joueur
- `check_collision(maze)` : Vérifie les collisions avec les murs
- `collect_point(points)` : Collecte des points
- `lose_life()` : Perd une vie
- `draw(screen)` : Dessine le joueur

### Enemy, Octopus, EnemyShip

Représentent les ennemis du jeu.

#### Attributs principaux

- `x`, `y` : Position de l'ennemi
- `speed` : Vitesse de déplacement
- `direction` : Direction actuelle
- `image` : Image de l'ennemi
- `rect` : Rectangle de collision

#### Méthodes principales

- `load_image(image_path)` : Charge l'image de l'ennemi
- `update(maze, player)` : Met à jour la position de l'ennemi
- `check_collision(maze)` : Vérifie les collisions avec les murs
- `change_direction()` : Change la direction de l'ennemi
- `check_player_collision(player)` : Vérifie les collisions avec le joueur
- `draw(screen)` : Dessine l'ennemi

### Maze

Représente le labyrinthe océanique.

#### Attributs principaux

- `width`, `height` : Dimensions du labyrinthe en nombre de cellules
- `cell_size` : Taille d'une cellule en pixels
- `grid` : Grille du labyrinthe
- `walls` : Liste des murs
- `points` : Liste des points
- `power_points` : Liste des points de pouvoir
- `wall_image` : Image des murs

#### Méthodes principales

- `init_empty_grid()` : Initialise une grille vide
- `load_level(level_data)` : Charge un niveau
- `load_wall_image(image_path)` : Charge l'image des murs
- `is_wall(x, y)` : Vérifie si la position donnée contient un mur
- `check_collision(rect)` : Vérifie si un rectangle est en collision avec un mur
- `collect_point(rect)` : Vérifie si un rectangle collecte un point
- `draw(screen)` : Dessine le labyrinthe
- `is_complete()` : Vérifie si tous les points ont été collectés

## États du jeu

Le jeu peut être dans l'un des états suivants :

- `menu` : Menu principal
- `playing` : Jeu en cours
- `pause` : Jeu en pause
- `level_transition` : Transition entre les niveaux
- `game_over` : Fin de partie (défaite)
- `victory` : Fin de partie (victoire)

## Contrôles

- Flèches directionnelles : Déplacer le bateau pirate
- Espace : Confirmer / Commencer le jeu / Passer au niveau suivant
- Échap : Pause / Retour au menu / Quitter
- M : Retour au menu

## Niveaux

Le jeu comprend trois niveaux de difficulté croissante :

1. **Mer des Caraïbes** : Niveau facile avec peu d'ennemis
2. **Détroit de Gibraltar** : Niveau moyen avec plus d'ennemis et un labyrinthe plus complexe
3. **Triangle des Bermudes** : Niveau difficile avec beaucoup d'ennemis et un labyrinthe très complexe

## Assets

### Images

Les sprites du jeu sont générés automatiquement en utilisant la bibliothèque Pillow :

- `player.png` : Bateau pirate (joueur)
- `octopus.png` : Pieuvre (ennemi)
- `enemy_ship.png` : Bateau ennemi
- `wall.png` : Mur (récif corallien)
- `point.png` : Point (pièce d'or)
- `power_point.png` : Point de pouvoir (coffre au trésor)

### Sons

Des placeholders pour les sons sont créés, mais ils peuvent être remplacés par des fichiers audio réels :

- `move.wav` : Son de déplacement du joueur
- `collect.wav` : Son de collecte des points
- `power.wav` : Son de collecte des points de pouvoir
- `hit.wav` : Son de collision avec un ennemi
- `game_over.wav` : Son de fin de partie
- `victory.wav` : Son de victoire
- `menu.wav` : Musique du menu
- `background.wav` : Musique de fond pendant le jeu

## Tests

Le module `test_game.py` contient des tests pour vérifier le bon fonctionnement du jeu :

- `test_game_initialization()` : Teste l'initialisation du jeu
- `test_level_loading()` : Teste le chargement des niveaux
- `test_player_movement()` : Teste le mouvement du joueur
- `test_enemy_movement()` : Teste le mouvement des ennemis
- `test_collision_detection()` : Teste la détection des collisions
- `test_point_collection()` : Teste la collecte des points
- `test_game_states()` : Teste les différents états du jeu

## Installation et configuration

### Prérequis
- Python 3.x

### Création d'un environnement virtuel (recommandé)

#### Sous Windows
```
# Création de l'environnement virtuel
python -m venv venv

# Activation de l'environnement virtuel
venv\Scripts\activate
```

#### Sous macOS/Linux
```
# Création de l'environnement virtuel
python3 -m venv venv

# Activation de l'environnement virtuel
source venv/bin/activate
```

### Installation des dépendances
Une fois l'environnement virtuel activé, installez les dépendances nécessaires :
```
pip install -r requirements.txt
```

Ou installez-les manuellement :
```
pip install pygame pillow
```

## Comment jouer

1. Exécutez `main.py` pour lancer le jeu
   ```
   python main.py
   ```
2. Dans le menu principal, appuyez sur Espace pour commencer
3. Utilisez les flèches directionnelles pour déplacer le bateau pirate
4. Collectez toutes les pièces d'or pour passer au niveau suivant
5. Évitez les pieuvres et les bateaux ennemis
6. Appuyez sur Échap pour mettre le jeu en pause

## Dépendances

- Python 3.x
- Pygame (gestion du jeu)
- Pillow (pour la génération des sprites)

## Améliorations possibles

- Ajout de power-ups (invincibilité temporaire, vitesse accrue, etc.)
- Ajout de niveaux supplémentaires
- Amélioration des graphismes et des animations
- Ajout d'un système de sauvegarde des meilleurs scores
- Ajout d'un mode multijoueur
- Ajout d'un éditeur de niveaux
