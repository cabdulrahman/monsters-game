# db/base.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Base class for models
Base = declarative_base()

# Setup database path
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "..", "monster_game.db")

# Create engine
engine = create_engine(f"sqlite:///{os.path.abspath(db_path)}")

# Create session factory
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
