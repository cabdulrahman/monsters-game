import random
from db.models import Player, PlayerMonster, MonsterSpecies
from db.base import session

def catch_monster(player):
    species = random.choice(session.query(MonsterSpecies).all())
    success_rate = calculate_catch_rate(species.rarity, player.level)

    if random.random() < success_rate:
        monster = PlayerMonster(
            nickname=species.name,
            level=1,
            current_hp=species.base_hp,
            player_id=player.id,
            species_id=species.id
        )
        session.add(monster)
        session.commit()
        print(f"\n You caught a {species.name}!")
        return monster
    else:
        print(f"\n The wild {species.name} escaped.")
        return None

def calculate_catch_rate(rarity, level):
    base = 0.4
    if rarity == "Rare":
        base = 0.2
    elif rarity == "Legendary":
        base = 0.1
    return base + (0.01 * level)

def view_monster_collection(player):
    monsters = session.query(PlayerMonster).filter_by(player_id=player.id).all()
    if not monsters:
        print("\n You have no monsters.")
        return []
    for m in monsters:
        print(f"{m.nickname} (Level {m.level})")
    return monsters


    print("\n===  YOUR MONSTER COLLECTION ===")
    for m in monsters:
        species = session.query(MonsterSpecies).filter_by(id=m.species_id).first()
        print(f"- {m.nickname} the {species.name} (Level {m.level}, HP: {m.current_hp})")

def train_monster(monster: PlayerMonster):
    print(f"\n Training {monster.nickname}...")
    exp_gain = random.randint(10, 25)
    monster.player.experience += exp_gain
    print(f"{monster.nickname} gained {exp_gain} EXP!")

    level_up_player(monster.player)
    check_evolution(monster)
    session.commit()

def level_up_player(player: Player):
    level_threshold = 100
    leveled_up = False

    while player.experience >= level_threshold:
        player.level += 1
        player.experience -= level_threshold
        leveled_up = True

    if leveled_up:
        print(f"\n {player.username} leveled up to Level {player.level}!")
        session.commit()

def check_evolution(player_monster: PlayerMonster):
    species = session.query(MonsterSpecies).filter_by(id=player_monster.species_id).first()
    if species.evolution_species_id and player_monster.level >= 10:
        evolved_species = session.query(MonsterSpecies).filter_by(id=species.evolution_species_id).first()
        if evolved_species:
            print(f"\n {player_monster.nickname} is evolving into {evolved_species.name}!")
            player_monster.species_id = evolved_species.id
            player_monster.current_hp = evolved_species.base_hp
            session.commit()
