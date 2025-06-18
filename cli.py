import sys
import random
from db.models import Player, PlayerMonster, MonsterSpecies
from db.base import session
from lib.player import catch_monster
from lib import battle, trade, player
from lib.trade import propose_trade


# Player Selection 
def select_player():
    players = session.query(Player).all()
    print("\nAvailable Players:")
    for p in players:
        print(f"{p.id}. {p.username}")

    while True:
        try:
            player_id = int(input("Enter your Player ID: "))
            player_obj = session.get(Player, player_id)
            if player_obj:
                return player_obj
            else:
                print("Player not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# ---------- Catch ----------
def catch_monster_menu(current_player):
    species_list = session.query(MonsterSpecies).all()
    if not species_list:
        print("No monsters available to catch. Seed the database first.")
        return

    species = random.choice(species_list)
    print(f"A wild {species.name} appeared!")
    player.catch_monster(current_player, species)

# ---------- Battle ----------
def start_battle(current_player):
    monsters = session.query(PlayerMonster).filter_by(player_id=current_player.id).all()
    if not monsters:
        print("You have no monsters to battle with!")
        return

    print("\nYour Monsters:")
    for m in monsters:
        print(f"{m.id}. {m.nickname} (Level: {m.level}, HP: {m.current_hp})")
    
    try:
        monster_id = int(input("Choose a monster by ID: "))
        monster = session.get(PlayerMonster, monster_id)

        wild_monsters = session.query(MonsterSpecies).all()
        print("\nWild Monsters:")
        for m in wild_monsters:
            print(f"{m.id}. {m.name} (HP: {m.base_hp})")
        wild_id = int(input("Choose a wild monster by ID: "))
        wild = session.get(MonsterSpecies, wild_id)

        if monster and wild:
            battle.start_battle(monster, wild)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

# ---------- Train ----------
def train_monster(current_player):
    monsters = session.query(PlayerMonster).filter_by(player_id=current_player.id).all()
    if not monsters:
        print("You have no monsters to train!")
        return

    print("\nYour Monsters:")
    for m in monsters:
        print(f"{m.id}. {m.nickname} (Level: {m.level}, XP: {m.experience}, HP: {m.current_hp})")
    
    try:
        monster_id = int(input("Choose a monster to train by ID: "))
        monster = session.get(PlayerMonster, monster_id)
        if monster:
            monster.experience += 10
            print(f"{monster.nickname} gained 10 XP!")
            session.commit()
        else:
            print("Invalid monster ID.")
    except ValueError:
        print("Please enter a valid number.")

# ---------- Collection ----------
def view_collection(current_player):
    monsters = session.query(PlayerMonster).filter_by(player_id=current_player.id).all()
    print(f"\n{current_player.username}'s Monster Collection:")
    for m in monsters:
        species = session.get(MonsterSpecies, m.species_id)
        print(f"- {m.nickname} (Species: {species.name}, Level: {m.level}, HP: {m.current_hp}, XP: {m.experience})")

# ---------- Trade ----------
def initiate_trade(current_player):
     propose_trade(current_player)


    
# ---------- Profile ----------
def view_profile(current_player):
    print(f"\nPlayer Profile:")
    print(f"Name: {current_player.username}")
    print(f"ID: {current_player.id}")
    print(f"Experience: {current_player.experience}")
    print(f"Money: ${current_player.money}")
    view_collection(current_player)

# ---------- Main Menu ----------
def main_menu():
    current_player = select_player()
    while True:
        print(f"\n=== Main Menu (Player: {current_player.username}) ===")
        print("1. Catch Monster")
        print("2. Battle Wild Monster")
        print("3. View Collection")
        print("4. Train Monster")
        print("5. Trade")
        print("6. Profile")
        print("7. Exit")
        choice = input("Select an action > ")

        if choice == "1":
          catch_monster_menu(current_player)

        elif choice == "2":
            start_battle(current_player)
        elif choice == "3":
            view_collection(current_player)
        elif choice == "4":
            train_monster(current_player)
        elif choice == "5":
            initiate_trade(current_player)
        elif choice == "6":
            view_profile(current_player)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
