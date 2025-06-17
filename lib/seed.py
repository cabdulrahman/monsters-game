import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import sessionmaker
from db.models import (
    engine, Player, MonsterSpecies, PlayerMonster,
    Ability, Achievement, MonsterType, Rarity
)

Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(PlayerMonster).delete()
session.query(Player).delete()
session.query(Ability).delete()
session.query(MonsterSpecies).delete()
session.query(Achievement).delete()
session.commit()

# Monster species data with corrected Enum usage for rarity
species_list = [
    {"name": "Inferno", "type": MonsterType.FIRE, "base_hp": 80, "base_attack": 90, "base_defense": 60, "rarity": Rarity.RARE},
    {"name": "Hydro", "type": MonsterType.WATER, "base_hp": 85, "base_attack": 70, "base_defense": 75, "rarity": Rarity.UNCOMMON},
    {"name": "Leafling", "type": MonsterType.GRASS, "base_hp": 75, "base_attack": 68, "base_defense": 72, "rarity": Rarity.UNCOMMON},
    {"name": "Zapfur", "type": MonsterType.ELECTRIC, "base_hp": 60, "base_attack": 95, "base_defense": 50, "rarity": Rarity.UNCOMMON},
    {"name": "Stonox", "type": MonsterType.GROUND, "base_hp": 95, "base_attack": 80, "base_defense": 85, "rarity": Rarity.RARE},
    {"name": "Blazebite", "type": MonsterType.FIRE, "base_hp": 78, "base_attack": 88, "base_defense": 62, "rarity": Rarity.UNCOMMON},
    {"name": "Aquadart", "type": MonsterType.WATER, "base_hp": 82, "base_attack": 73, "base_defense": 70, "rarity": Rarity.UNCOMMON},
    {"name": "Thornjaw", "type": MonsterType.GRASS, "base_hp": 77, "base_attack": 70, "base_defense": 74, "rarity": Rarity.UNCOMMON},
    {"name": "Voltspark", "type": MonsterType.ELECTRIC, "base_hp": 61, "base_attack": 92, "base_defense": 52, "rarity": Rarity.UNCOMMON},
    {"name": "Tremortusk", "type": MonsterType.GROUND, "base_hp": 97, "base_attack": 79, "base_defense": 88, "rarity": Rarity.RARE},
    {"name": "Emberlynx", "type": MonsterType.FIRE, "base_hp": 76, "base_attack": 85, "base_defense": 64, "rarity": Rarity.UNCOMMON},
    {"name": "Wavefin", "type": MonsterType.WATER, "base_hp": 88, "base_attack": 71, "base_defense": 76, "rarity": Rarity.UNCOMMON},
    {"name": "Fernox", "type": MonsterType.GRASS, "base_hp": 74, "base_attack": 69, "base_defense": 73, "rarity": Rarity.UNCOMMON},
    {"name": "Sparkhorn", "type": MonsterType.ELECTRIC, "base_hp": 59, "base_attack": 96, "base_defense": 49, "rarity": Rarity.UNCOMMON},
    {"name": "Cragbeast", "type": MonsterType.GROUND, "base_hp": 99, "base_attack": 78, "base_defense": 90, "rarity": Rarity.EPIC},
    {"name": "Scorchy", "type": MonsterType.FIRE, "base_hp": 79, "base_attack": 86, "base_defense": 63, "rarity": Rarity.UNCOMMON},
    {"name": "Coralisk", "type": MonsterType.WATER, "base_hp": 84, "base_attack": 72, "base_defense": 77, "rarity": Rarity.UNCOMMON},
    {"name": "Mossmite", "type": MonsterType.GRASS, "base_hp": 76, "base_attack": 67, "base_defense": 71, "rarity": Rarity.UNCOMMON},
    {"name": "Electrowl", "type": MonsterType.ELECTRIC, "base_hp": 62, "base_attack": 93, "base_defense": 53, "rarity": Rarity.UNCOMMON},
    {"name": "Rockzilla", "type": MonsterType.GROUND, "base_hp": 100, "base_attack": 82, "base_defense": 91, "rarity": Rarity.EPIC},
]

species_instances = [MonsterSpecies(**data) for data in species_list]

# Abilities (linked to the first 5 monster species for example purposes)
abilities = [
    Ability(name="Fire Blast", description="A strong fire attack causing burn", species=species_instances[0]),
    Ability(name="Aqua Ring", description="Restores some HP every turn", species=species_instances[1]),
    Ability(name="Leaf Tornado", description="May lower enemy accuracy", species=species_instances[2]),
    Ability(name="Thunder Fang", description="High-voltage bite that may paralyze", species=species_instances[3]),
    Ability(name="Rock Slide", description="Hits all enemies, may cause flinch", species=species_instances[4]),
]

# Players
player_ash = Player(username="AshKetchum", level=10, experience=1500, money=300.0)
player_misty = Player(username="MistyW", level=8, experience=1100, money=250.0)
player_brock = Player(username="Brock", level=7, experience=1000, money=200.0)
player_jessie = Player(username="Jessie", level=9, experience=1200, money=270.0)
player_james = Player(username="James", level=9, experience=1150, money=260.0)

# Achievements
first_win = Achievement(name="First Victory", description="Won the first battle")
player_ash.achievements.append(first_win)

# Player Monsters
monster1 = PlayerMonster(
    nickname="Blaze", level=10, current_hp=78, experience=1300,
    owner=player_ash, species=species_instances[0]
)
monster2 = PlayerMonster(
    nickname="Splashy", level=9, current_hp=82, experience=1200,
    owner=player_misty, species=species_instances[1]
)

# Add all records
session.add_all(
    species_instances +
    abilities +
    [player_ash, player_misty, player_brock, player_jessie, player_james] +
    [first_win, monster1, monster2]
)

session.commit()

print("✅ Database seeded with monster species, abilities, players, and player monsters.")
