import random
from datetime import datetime
from db.models import Player, PlayerMonster, MonsterSpecies, Battle
from sqlalchemy.orm import Session

def calculate_damage(attacker_level, base_attack, defender_base_defense):
    return max(1, (attacker_level * base_attack // 2) - (defender_base_defense // 2))


def battle(player: Player, player_monster: PlayerMonster, ai_monster: PlayerMonster, session: Session):
    print(f"\n Battle Started: {player.username} vs {ai_monster.nickname}")
    player_turn = True
    log = []

    while player_monster.current_hp > 0 and ai_monster.current_hp > 0:
        if player_turn:
            damage = calculate_damage(player_monster.level, player_monster.species.base_attack, ai_monster.species.base_defense)
            ai_monster.current_hp -= damage
            log.append(f"{player_monster.nickname} hits {ai_monster.nickname} for {damage} damage!")
        else:
            damage = calculate_damage(ai_monster.level, ai_monster.species.base_attack, player_monster.species.base_defense)
            player_monster.current_hp -= damage
            log.append(f"{ai_monster.nickname} hits {player_monster.nickname} for {damage} damage!")
        
        player_turn = not player_turn

    if player_monster.current_hp > 0:
        outcome = "win"
        log.append(f" {player.username}'s {player_monster.nickname} won the battle!")
        apply_rewards(player, session)
    else:
        outcome = "loss"
        log.append(f" {player.username}'s {player_monster.nickname} lost the battle.")

    battle = Battle(
        player_id=player.id,
        player_monster_id=player_monster.id,
        opponent_name=ai_monster.nickname,
        outcome=outcome,
        timestamp=datetime.utcnow()
    )
    session.add(battle)
    session.commit()

    print("\n".join(log))
    return outcome

def apply_rewards(player: Player, session: Session):
    player.experience += 50
    player.money += 100
    session.commit()
    print(f" {player.username} earned 50 XP and 100 coins!")

    if random.random() < 0.1:  
        rare_species = session.query(MonsterSpecies).order_by(MonsterSpecies.rarity.desc()).first()
        rare_monster = PlayerMonster(
            nickname=f"Rare {rare_species.name}",
            level=5,
            current_hp=rare_species.base_hp,
            species=rare_species,
            owner=player
        )
        session.add(rare_monster)
        session.commit()
        print(f" {player.username} received a rare monster: {rare_species.name}!")

def generate_ai_monster(session: Session):
    species = random.choice(session.query(MonsterSpecies).all())
    ai_monster = PlayerMonster(
        nickname=f"AI {species.name}",
        level=5,
        current_hp=species.base_hp,
        species = species,
        species_id=species.id, 
    )
    return ai_monster