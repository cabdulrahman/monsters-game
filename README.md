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
 cd ..
 python lib/seed.py
 

## Running the Game
 python cli.py

## Running Tests
 Run the following to test gameplay features like player creation, monster battles, and more:

 python -m tests.test_game
 python -m tests.test_battle
## Game Instructions
   Welcome to the Monster Game! Embark on a journey to collect, train, and battle unique monsters. Below is a guide to help you navigate and enjoy the game.
   Game Start
   1. Launch the game from your terminal:
    python cli.py
   2. You'll see a list of available players:
      Available Players:
       1. AshKetchum
       2. MistyW
         ...
  3. Enter the Player ID number to select your character:
      Enter your Player ID: 1

  ## Main Menu Options
  Once logged in, you'll see the Main Menu:

   Main Menu (Player: AshKetchum)
    1. Catch Monster
    2. Battle Wild Monster
    3. View Collection
    4. Train Monster
    5. Trade
    6. Profile
    7. Exit
Here's what each option does:

1.  Catch Monster
Go on a hunt to catch a wild monster.

The monster's type, rarity, and stats are randomized.

If successful, it gets added to your collection.

2. Battle Wild Monster
Choose one of your monsters to battle a wild one.

Win to earn experience, level up, and possibly unlock achievements.

Outcomes: Win / Lose / Draw (affects monster stats and player XP).

3. View Collection
View all the monsters you currently own.

See their nickname, level, HP, type, and species stats.

4. Train Monster
Choose a monster to train and improve.

Increases experience and can lead to level-ups.

Useful for preparing for tougher battles.

5. Trade
Trade monsters with other players.

You select a monster to offer and one to request.

Both players must accept for the trade to complete.

6. Profile
View your player profile:

Level

Experience

Money

Achievements earned

7. 🚪 Exit
Save your progress and exit the game.


## Technologies used
 Python 3: The core programming language.

 SQLAlchemy: ORM (Object Relational Mapper) for database interactions with SQLite.

 SQLite: A lightweight, file-based database for persistence.

## Database Schema

The Monster Game uses a relational database to manage players, monsters, battles, trades, and achievements.

You can explore the schema visually here:  
 [Monster Game Database Schema on dbdiagram.io](https://dbdiagram.io/d/Monster-Game-Database-Schema-6852b853f039ec6d36cce3c6)

 ##  Demo Video

Watch the gameplay demo here: [Monster Game Demo](https://drive.google.com/file/d/1g7CcokE9PD4i22syerNX8nA1IMd7fI-B/view?usp=sharing)



