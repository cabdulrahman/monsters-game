from db.models import Player, PlayerMonster, MonsterSpecies
from db.base import session

def trade_monster(sender_username, receiver_username, monster_id):
    sender = session.query(Player).filter_by(username=sender_username).first()
    receiver = session.query(Player).filter_by(username=receiver_username).first()

    if not sender or not receiver:
        print("One of the players does not exist.")
        return

    monster = session.query(PlayerMonster).filter_by(id=monster_id, player_id=sender.id).first()
    if not monster:
        print("Monster not found or does not belong to the sender.")
        return

    monster.player_id = receiver.id
    session.commit()
    print(f"{sender_username} successfully traded {monster.nickname} to {receiver_username}!")

def list_player_monsters(username):
    player = session.query(Player).filter_by(username=username).first()
    if not player:
        print("Player not found.")
        return []

    monsters = session.query(PlayerMonster).filter_by(player_id=player.id).all()
    for m in monsters:
        print(f"[{m.id}] {m.nickname} (Lv {m.level})")
    return monsters

def propose_trade(player):
    print("\n--- Propose Trade ---")
    list_player_monsters(player.username)

    # Show other available players
    print("\nAvailable Players:")
    all_players = session.query(Player).filter(Player.id != player.id).all()
    for p in all_players:
        print(f"- {p.username}")

    monster_id = input("Enter the ID of the monster you want to trade: ")
    target_username = input("Enter the username of the player you want to trade with: ")

    trade_monster(player.username, target_username, monster_id)

