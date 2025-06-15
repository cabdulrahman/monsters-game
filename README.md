## Monster Game
Monster Game is a terminal-based monster training, battling, and trading game built with Python. Players can collect, level up, and trade monsters of different elemental types while battling opponents in a turn-based system. The game uses SQLAlchemy for ORM and SQLite for persistent storage.

## Features
20+ Unique Monster Species with elemental types (Fire, Water, Grass, Electric, Ground, and more)

 Turn-Based Battle System

 Monster Trading between players

 Player Progression with levels and experience points (XP)

 Achievements for special milestones

 SQLAlchemy ORM Integration

 Modular and Extensible Codebase

## Folder Structure
monster_game/
├── cli.py               # Main terminal interface to start the game
├── db/
│   ├── base.py          # SQLAlchemy setup and models
│   ├── create_db.py     # Script to create the database
│   └── reset_db.py      # Script to reset the database
├── lib/
│   ├── player.py        # Player management and authentication
│   ├── battle.py        # Battle logic and outcomes
│   ├── trade.py         # Monster trading logic
│   └── seed.py          # Seed file for initial data
├── tests/
│   ├── test_game.py     # Unit tests for core gameplay
│   └── test_battle.py   # Unit tests for battle system
├── requirements.txt     # Project dependencies
└── README.md            # This documentation

## Setup Instructions
1. Clone the repository
 git clone https://github.com/Harshpal01/monster_game.git
 cd monster_game
2. Set up a virtual environment
 python3 -m venv venv
 source venv/bin/activate
3. Install dependencies
 pip install Pipfile

## Database Setup
 cd db
 python create_db.py
 python reset_db.py
 cd lib
 python lib/seed.py
 cd ..
 
## Running the Game
 python cli.py

## Running Tests
 Run the following to test gameplay features like player creation, monster battles, and more:

 python -m tests.test_game
 python -m tests.test_battle

## Gameplay Overview
 Select or create a player

 Catch and manage monsters

 Battle AI or other players

 Trade monsters with other players

 Level up and earn achievements

# Author
 Dominic Kipkorir
🔗 GitHub: Harshpal01

