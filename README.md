## Monster Game
Monster Game is a terminal-based monster training, battling, and trading game built with Python. Players can collect, level up, and trade monsters of different elemental types while battling opponents in a turn-based system. The game uses SQLAlchemy for ORM and SQLite for persistent storage.

## Features
 1. Turn-Based Battle System
Engage in classic turn-based battles where speed, attack, and defense stats determine the outcome. Use tactics, type advantages, and monster levels to win fights.

 2. Player Progression
Players earn Experience Points (XP) by battling or training. Leveling up unlocks new abilities, strengthens monsters, and can even trigger monster evolution.

 3. Monster Training
Choose which monster to train and gain XP through specialized routines. This allows your monsters to improve outside of battle, giving you an edge in future encounters.

 4. Achievements System
Track your milestones and earn achievements for goals such as winning 10 battles, evolving a monster, or trading with 5 players.

 5. Monster Trading
Trade monsters with other players. This system enables co-op style gameplay and adds a social layer to your in-game progression.

 6. Modular and Extensible Codebase
The codebase is organized into modules such as battle_engine, game_logic, and player, making it easy to extend functionality (e.g., add quests, more types, AI enemies).

 7. SQLite with SQLAlchemy ORM
Persistent storage of player data, monsters, and battles using SQLAlchemy. Easily switch to another database backend in the future.

8. Testing Suite
Includes unit tests for battle logic, game progression, and monster management — ensuring the game is reliable and maintainable.

## Folder Structure
monster_game/
├── cli.py                  # Main terminal interface to start the game
├── db/
│   ├── base.py             # SQLAlchemy engine, Base, and session setup
│   ├── models.py           # All database models and relationships
│   ├── create_db.py        # Script to create the database
│   └── reset_db.py         # Script to reset the database
├── lib/
│   ├── player.py           # Player management and authentication
│   ├── battle.py           # Battle coordination logic (e.g. player vs. player)
│   ├── battle_engine.py    # Turn-based combat engine logic
│   ├── game_logic.py       # General game loop and gameplay mechanics
│   ├── monster.py          # Monster-related utility functions
│   ├── trade.py            # Monster trading logic
│   └── seed.py             # Seed file for initial data
├── tests/
│   ├── test_game.py        # Unit tests for core gameplay
│   └── test_battle.py      # Unit tests for battle system
├── requirements.txt        # Project dependencies
└── README.md               # This documentation

## Setup Instructions
1. Clone the repository
 git clone https://github.com/cabdulrahman/monsters-game
 cd monster_game
2. Set up a virtual environment
 pipenv install
 pipenv shell
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

## Technologies used
 Python 3: The core programming language.

 SQLAlchemy: ORM (Object Relational Mapper) for database interactions with SQLite.

 SQLite: A lightweight, file-based database for persistence.

# Author
 Dominic Kipkorir
🔗 GitHub: Harshpal01

