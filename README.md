# Space Invaders

## Overview
This project is a simple yet engaging game developed using the Pygame module in Python, for the Computer Science Project in grade 12 at Bala Vidya Mandir. It involves creating a game window, adding images and movement mechanics, detecting keyboard inputs and collisions, and incorporating sounds and background music. The player controls a character navigating through obstacles, collecting items, and avoiding enemies.

## Features
- **Game Window**: A visually appealing game window with custom dimensions.
- **Sprites and Images**: Character and environment sprites, background images, and UI elements.
- **Movement Mechanics**: Smooth character movement controlled by keyboard inputs.
- **Collision Detection**: Detecting collisions between the player and obstacles/enemies.
- **Sound and Music**: Background music and sound effects for interactions and events.
- **Score System**: A simple scoring system to track player progress.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/space-indvaders.git
   cd pygame-space-invaders
   ```
2. **Install dependencies:**
   Ensure you have Python installed (preferably 3.7 or later). Install Pygame using pip:
   ```bash
   pip install pygame
   ```

## Running the Game
To run the game, execute the following command in your terminal:
```bash
python main.py
```

## Gameplay Instructions
- **Start the Game**: Launch the game by running `main.py`.
- **Movement**: Use the arrow keys to move your character.
  - **Left Arrow**: Move left
  - **Right Arrow**: Move right
  - **Up Arrow**: Jump
- **Objective**: Navigate through the level, avoid enemies, and collect items to score points.
- **Score**: Collect items to increase your score. Avoid enemies to stay alive.

## Code Structure
- **main.py**: The main game file that initializes the game and contains the game loop.
- **settings.py**: Configuration file for game settings such as screen dimensions and colors.
- **player.py**: Defines the player character and movement mechanics.
- **enemy.py**: Defines enemy behavior and collision detection.
- **item.py**: Defines collectible items and their interactions.
- **game_functions.py**: Helper functions for game initialization and main game loop operations.
- **assets/**: Directory containing images, sounds, and music files used in the game.

## Adding Your Own Assets
To customize the game with your own images and sounds:
1. Place your image files in the `assets/images/` directory.
2. Place your sound files in the `assets/sounds/` directory.
3. Update the file paths in the relevant classes (e.g., `player.py`, `enemy.py`, `item.py`) to use your new assets.

## Future Enhancements
- **Levels**: Adding multiple levels with increasing difficulty.
- **Power-Ups**: Introducing power-ups that give temporary advantages.
- **High Score System**: Implementing a high score system to track the best scores.

## Troubleshooting
- **Game not starting**: Ensure Pygame is correctly installed and your Python version is compatible.
- **Images not loading**: Verify the paths to your image files are correct.
- **Sound issues**: Ensure the sound files are in the correct format and paths are correctly specified.

## Credits
This game was developed as a learning project using @attreyabhatt's tutorial on FreeCodeCamp on YouTube.
