Assignment for Advanced Programming class (WiSe '23) 

by Ipshita Singh - Matriculation No.: 3121217

![tests](https://github.com/IpshitaSingh/Alien-Run/workflows/tests/badge.svg)

# Alien Run

Alien Run is a 2D game developed using Pygame, where the player controls a character, referred to as _Alien_, and navigates through obstacles while avoiding the enemy.

## Table of Contents

- [Features](#features)
- [UML Diagrams](#uml-diagrams)
- [Installation](#installation)
- [CI/CD Pipeline](#cicd-pipline)
- [Tests](#tests)

## Features

1. Player Control: Player can control the _Alien_ using simple keyboard inputs, allowing for smooth and responsive movement throughout the game.

2. Obstacle Course: The game features an obstacle course filled with moving obstacles, which players must navigate to progress. The velocity of obstacles increase with level upgrades.

3. Enemy Encounters: Player must avoid enemy encounters as they traverse the obstacle course. The enemy dynamically moves and changes direction, adding an element of challenge and strategy to the gameplay.

4. Scoring System: Alien Run incorporates a scoring system where the player earns points for successfully surviving and avoiding collisions.
     - Player earns 250 points for surviving 10 seconds. After 10 seconds, the timer resets, and a new 10-second interval starts. 
     - Player loses 10 points upon colliding with obstacles or enemies.

5. Level Progression: As the player accumulates points, they progress through different levels of increasing difficulty. With each new level, the velocity with which obstacles move increases, keeping the gameplay fresh and engaging.
    - Upon reaching 500 points, the player advances to level 2. Subsequent levels are reached at intervals of 500 points (e.g., 1000 points for level 3, 1500 points for level 4, and so on).

6. Sound Effects: Immersive sound effects, including background music and collision sounds, enhance the gaming experience, providing the player with auditory feedback as they play.

## UML Diagrams

## Installation

## CICD Pipeline
The CI/CD pipeline is set up using GitHub Actions. On each push to the main branch, the pipeline performs the following steps:

1. **Code Versioning:** Git for version control.
2. **Continuous Integration:** GitHub Actions for automated workflows.
3. **Build Management:** setuptools for streamlined project builds.
4. **Testing:** pytest for unit testing.

## Tests
Unit tests are implemented using pytest in [test_game.py](https://github.com/IpshitaSingh/Alien-Run/blob/main/test_game.py). The **CI/CD pipeline** runs these tests to ensure the proper functioning of the game.
### First Test: Obstacles
This test checks if obstacle creation is performed as intended.
### Second Test: Collision
This test checks if the collisions between _Alien_ and obstacles or enemy is detected.
### Third Test: Score
This test checks if the score updation is functioning as intended, based on the time survived.
