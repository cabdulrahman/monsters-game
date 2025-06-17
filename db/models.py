from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean,
    ForeignKey, Table, DateTime, Enum as SQLEnum, Text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from datetime import datetime
import os

Base = declarative_base()

# Enum for monster types
class MonsterType(PyEnum):
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECTRIC = "Electric"
    GROUND = "Ground"
    ROCK = "Rock"
    ICE = "Ice"
    FLYING = "Flying"
    DARK = "Dark"
    PSYCHIC = "Psychic"
    STEEL = "Steel"
    GHOST = "Ghost"
    BUG = "Bug"
    DRAGON = "Dragon"
    NORMAL = "Normal"
    FAIRY = "Fairy"

# Enum for rarity types
class Rarity(PyEnum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"

# Enum for battle outcomes
class BattleResult(PyEnum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"

# Association table for player achievements
player_achievements = Table(
    'player_achievements',
    Base.metadata,
    Column('player_id', ForeignKey('players.id'), primary_key=True),
    Column('achievement_id', ForeignKey('achievements.id'), primary_key=True)
)

# Association table for monster abilities (many-to-many)
monster_abilities = Table(
    'monster_abilities',
    Base.metadata,
    Column('monster_species_id', ForeignKey('monster_species.id'), primary_key=True),
    Column('ability', String, primary_key=True)
)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    money = Column(Float, default=0.0)

    # Relationships
    monsters = relationship('PlayerMonster', back_populates='owner')
    achievements = relationship('Achievement', secondary=player_achievements, back_populates='players')
    battles = relationship('Battle', back_populates='player', foreign_keys='Battle.player_id')
    trades_sent = relationship('Trade', back_populates='sender', foreign_keys='Trade.sender_id')
    trades_received = relationship('Trade', back_populates='receiver', foreign_keys='Trade.receiver_id')

class MonsterSpecies(Base):
    __tablename__ = 'monster_species'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(SQLEnum(MonsterType, name="monster_type", native_enum=False))
    base_hp = Column(Integer)
    base_attack = Column(Integer)
    base_defense = Column(Integer)
    rarity = Column(SQLEnum(Rarity, name="rarity_enum", native_enum=False))
    
    abilities = relationship('Ability', back_populates='species')
    evolution_species_id = Column(Integer, ForeignKey('monster_species.id'), nullable=True)
    evolution_species = relationship("MonsterSpecies", remote_side="[MonsterSpecies.id]")

class Ability(Base):
    __tablename__ = 'abilities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

    species_id = Column(Integer, ForeignKey('monster_species.id'))
    species = relationship('MonsterSpecies', back_populates='abilities')

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    level = Column(Integer, default=1)
    current_hp = Column(Integer, nullable=False)
    experience = Column(Integer, default=0)

    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))

    owner = relationship('Player', back_populates='monsters')
    species = relationship('MonsterSpecies')

class Battle(Base):
    __tablename__ = 'battles'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player_monster_id = Column(Integer, ForeignKey('player_monsters.id'))
    opponent_name = Column(String)
    outcome = Column(SQLEnum(BattleResult, name="battle_result_enum", native_enum=False))
    timestamp = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player", back_populates="battles")
    player_monster = relationship("PlayerMonster")

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('players.id'))
    receiver_id = Column(Integer, ForeignKey('players.id'))
    offered_monster_id = Column(Integer, ForeignKey('player_monsters.id'))
    requested_monster_id = Column(Integer, ForeignKey('player_monsters.id'))
    accepted = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship('Player', foreign_keys=[sender_id], back_populates='trades_sent')
    receiver = relationship('Player', foreign_keys=[receiver_id], back_populates='trades_received')

class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(Text)

    players = relationship('Player', secondary=player_achievements, back_populates='achievements')


# DATABASE CONNECTION 
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "..", "monster_game.db")
engine = create_engine(f"sqlite:///{os.path.abspath(db_path)}")
