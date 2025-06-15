from lib.player import create_player, login_player
from lib.monster import catch_monster, view_monster_collection
from db.base import session
from db.models import Player, PlayerMonster

def reset_test_data():
    """Optional: Clear test user data (for repeated testing)"""
    test_player = session.query(Player).filter_by(username="testuser").first()
    if test_player:
        session.query(PlayerMonster).filter_by(player_id=test_player.id).delete()
        session.delete(test_player)
        session.commit()
        print("Test data reset.")

def test_duplicate_username():
    print("\nTest: Duplicate Username")
    create_player("testuser")
    result = create_player("testuser")  
    assert result is None
    print("Passed: Duplicate username rejected")

def test_login_player():
    print("\nTest: Login Existing Player")
    player = login_player("testuser")
    assert player is not None
    print(f"Passed: Logged in as {player.username}")

def test_catch_monster():
    print("\nTest: Catch Monster")
    player = session.query(Player).filter_by(username="testuser").first()
    monster = catch_monster(player)
    assert monster is None or isinstance(monster, PlayerMonster)
    if monster:
        print(f"Passed: Caught {monster.nickname}")
    else:
        print("Passed: Monster escaped (still valid)")

def test_view_monster_collection():
    print("\nTest: View Monster Collection")
    player = session.query(Player).filter_by(username="testuser").first()
    monsters = view_monster_collection(player)
    assert monsters is not None 
    print(f"Passed: Viewed {len(monsters)} monster(s)")


if __name__ == "__main__":
    reset_test_data()          
    test_duplicate_username()
    test_login_player()
    test_catch_monster()
    test_view_monster_collection()
