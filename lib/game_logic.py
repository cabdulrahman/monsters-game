from db.base import session
from db.models import Player, PlayerMonster, MonsterSpecies
from lib.player import create_player, login_player, view_player_info
from lib.monster import catch_monster, view_monster_collection
from lib.battle import start_battle
from lib.trade import propose_trade, view_trades, accept_trade

def main_menu():
    print("\n=== MONSTER BATTLE CLI ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

def game_menu(player):
    print(f"\n--- Welcome {player.username} ---")
    print("1. Explore & Catch Monsters")
    print("2. View Your Monsters")
    print("3. Start Battle")
    print("4. View Profile")
    print("5. Propose Trade")
    print("6. View Pending Trades")
    print("7. Accept Trade")
    print("8. Logout")
    return input("Choose an action: ")

def start_game():
    player = None
    while True:
        choice = main_menu()

        if choice == "1":
            username = input("Enter a username to register: ")
            player = create_player(username)
        elif choice == "2":
            username = input("Enter your username to login: ")
            player = login_player(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
            continue

        while player:
            action = game_menu(player)

            if action == "1":
                catch_monster(player)
            elif action == "2":
                view_monster_collection(player)
            elif action == "3":
                start_battle(player)
            elif action == "4":
                view_player_info(player)
            elif action == "5":
                propose_trade(player)
            elif action == "6":
                view_trades(player)
            elif action == "7":
                accept_trade(player)
            elif action == "8":
                print(f"Logging out {player.username}...")
                player = None
            else:
                print("Invalid option.")
