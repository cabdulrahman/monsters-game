from sqlalchemy.orm import sessionmaker
from db.models import engine, Player, PlayerMonster, MonsterSpecies
from lib.battle_engine import battle, generate_ai_monster

Session = sessionmaker(bind=engine)
session = Session()

player = session.query(Player).filter_by(username="AshKetchum").first()
if not player:
    player = Player(username="AshKetchum", money=100, experience=0)
    session.add(player)
    session.commit()
    print("Created player AshKetchum")

player_monster = session.query(PlayerMonster).filter_by(player_id=player.id).first()
if not player_monster:

    species = session.query(MonsterSpecies).filter_by(name="Pikachu").first()
    if not species:
        species = MonsterSpecies(name="Pikachu", base_hp=50, base_attack=12, base_defense=8)
        session.add(species)
        session.commit()
        print("Created monster species Pikachu")

  
    player_monster = PlayerMonster(
        player_id=player.id,
        species_id=species.id,
        nickname="Sparky",
        level=5,
        current_hp=species.base_hp  
    )

    session.add(player_monster)
    session.commit()
    print(" Assigned monster 'Sparky' to AshKetchum")


ai_monster = generate_ai_monster(session)
if player_monster.current_hp is None:
    player_monster.current_hp = player_monster.species.base_hp

if ai_monster.current_hp is None:
    ai_monster.current_hp = ai_monster.species.base_hp
battle(player, player_monster, ai_monster, session)
