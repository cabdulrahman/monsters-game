import random
from db.models import Battle, Player, PlayerMonster, MonsterSpecies
from db.models import MonsterSpecies
from db.base import session
from .player import level_up_player

def create_battle(player1_id, player2_id, monster_teams) -> dict:
    battle = Battle(
        player_id=player1_id,
        opponent_name=f"Player {player2_id}",
        outcome="in_progress"
    )
    session.add(battle)
    session.commit()
    return {"battle_id": battle.id, "player1_id": player1_id, "player2_id": player2_id, "status": "started"}

def execute_turn(battle_id, attacker_monster, defender_monster, move) -> dict:
    move_power = move.get("power", random.randint(5, 15))
    type_effectiveness = move.get("effectiveness", 1.0)

    damage = calculate_damage(attacker_monster.stats, defender_monster.stats, move_power, type_effectiveness)
    defender_monster.current_hp = max(defender_monster.current_hp - damage, 0)
    session.commit()

    return {
        "battle_id": battle_id,
        "attacker": attacker_monster.nickname,
        "defender": defender_monster.nickname,
        "damage": damage,
        "defender_remaining_hp": defender_monster.current_hp
    }


def calculate_damage(attacker_stats, defender_stats, move_power, type_effectiveness) -> int:
    base_damage = ((attacker_stats["attack"] / max(1, defender_stats["defense"])) * move_power)
    return int(base_damage * type_effectiveness)

def check_battle_end(battle_id) -> bool:
    battle = session.query(Battle).get(battle_id)
    return battle.outcome in ["win", "loss"]


def apply_status_effects(monster_id, effect_type) -> None:
    monster = session.query(MonsterSpecies).get(monster_id)
    if effect_type == "poison":
        monster.current_hp = max(monster.current_hp - 5, 0)
    elif effect_type == "heal":
        monster.current_hp = min(monster.current_hp + 10, monster.max_hp)
    session.commit()

def calculate_battle_rewards(winner_id, battle_difficulty) -> tuple:
    base_exp = 50
    base_money = 20
    multiplier = {"easy": 1, "medium": 2, "hard": 3}.get(battle_difficulty, 1)

    gained_exp = base_exp * multiplier
    gained_money = base_money * multiplier

    player = session.query(Player).get(winner_id)
    player.experience += gained_exp
    player.money += gained_money
    session.commit()

    return gained_exp, gained_money

def create_ai_opponent(difficulty_level) -> dict:
    ai_stats = {
        "easy": {"attack": 10, "defense": 5, "hp": 30},
        "medium": {"attack": 15, "defense": 10, "hp": 50},
        "hard": {"attack": 20, "defense": 15, "hp": 70},
    }.get(difficulty_level, {"attack": 10, "defense": 5, "hp": 30})

    ai_monster = MonsterSpecies(
        name=f"AI_{difficulty_level}_Monster",
        stats=ai_stats,
        current_hp=ai_stats["hp"],
        max_hp=ai_stats["hp"]
    )
    session.add(ai_monster)
    session.commit()

    return {"ai_monster_id": ai_monster.id, "stats": ai_stats}

def propose_trade(from_player, to_player, offered_monsters, requested_monsters):
    print(f"{from_player.name} proposes a trade to {to_player.name}:")
    print(f"Offering: {[m.nickname for m in offered_monsters]}")
    print(f"Requesting: {[m.nickname for m in requested_monsters]}")
   
    return {
        "from": from_player.name,
        "to": to_player.name,
        "offer": [m.id for m in offered_monsters],
        "request": [m.id for m in requested_monsters]
    }

def record_battle(player_monster, opponent_name, outcome):
    battle = Battle(
        player_id=player_monster.player_id,
        player_monster_id=player_monster.id,
        opponent_name=opponent_name,
        outcome=outcome
    )
    session.add(battle)
    session.commit()


def reward_player(player):
    gained_exp = 50
    gained_money = 20
    player.experience += gained_exp
    player.money += gained_money
    print(f"\nYou earned {gained_exp} EXP and ${gained_money}!")
    session.commit()


def start_battle(player_monster, wild_monster_species):
    print(f"\nA wild {wild_monster_species.name} appears!")

    wild_hp = wild_monster_species.base_hp
    player_hp = player_monster.current_hp
    turn = 1
    wild_defending = False
    player_defending = False

    while player_hp > 0 and wild_hp > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"Your {player_monster.nickname} HP: {player_hp}")
        print(f"Wild {wild_monster_species.name} HP: {wild_hp}")

        move = input("Choose an action: 1. Attack 2. Defend > ")
        if move == "1":
            damage = random.randint(5, 15)
            if wild_defending:
                damage = int(damage * 0.5)
            wild_hp -= damage
            print(f"You dealt {damage} damage!")
            player_defending = False
        elif move == "2":
            print("You brace yourself.")
            player_defending = True
        else:
            print("Invalid input.")
            player_defending = False

        if wild_hp > 0:
            ai_move = random.choice(["attack", "defend"])
            if ai_move == "attack":
                damage = random.randint(4, 12)
                if player_defending:
                    damage = int(damage * 0.5)
                player_hp -= damage
                print(f"Wild attacks for {damage} damage!")
                wild_defending = False
            else:
                wild_defending = True
                print("Wild monster defends!")

        turn += 1

    if player_hp > 0:
        print(f"\n You defeated the wild {wild_monster_species.name}!")
        player_monster.current_hp = max(player_hp, 1)
        reward_player(player_monster.player)
        level_up_player(player_monster.player)
        record_battle(player_monster, wild_monster_species.name, "win")
    else:
        print(f"\n Your {player_monster.nickname} has fainted.")
        player_monster.current_hp = 0
        record_battle(player_monster, wild_monster_species.name, "loss")

    session.commit()
