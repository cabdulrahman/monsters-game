from db.models import Player, PlayerMonster, MonsterSpecies
from db.base import session
import random

def create_player(username):
    if session.query(Player).filter_by(username=username).first():
        print("Username already exists.")
        return None
    new_player = Player(username=username, level=1, experience=0, money=100)
    session.add(new_player)
    session.commit()
    print(f"Player '{username}' created successfully!")
    return new_player

def login_player(username):
    player = session.query(Player).filter_by(username=username).first()
    if not player:
        print("Player not found.")
        return None
    print(f"Welcome back, {player.username}!")
    return player

def level_up_player(player):
    player.experience += 50
    if player.experience >= player.level * 100:
        player.level += 1
        player.experience = 0
        print(f"{player.username} leveled up to Level {player.level}!")
    session.commit()

def view_player_info(player):
    print("\n=== PLAYER PROFILE ===")
    print(f"Username: {player.username}")
    print(f"Level: {player.level}")
    print(f"Experience: {player.experience}")
    print(f"Money: ${player.money}")

def catch_monster(player, species):
    success_chance = 0.8  
    if random.random() < success_chance:
        nickname = input(f"You caught a {species.name}! Give it a nickname: ")
        new_monster = PlayerMonster(
            nickname=nickname,
            player_id=player.id,
            species_id=species.id,
            current_hp=species.base_hp
        )
        session.add(new_monster)
        session.commit()
        print(f"{nickname} was added to your collection.")
        level_up_player(player)
    else:
        print(f"The {species.name} escaped!")
