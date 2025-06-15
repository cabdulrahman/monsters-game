import os
import sys

# Ensure the parent directory (project root) is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models import Base
from db.base import engine

if __name__ == "__main__":
    print(" Dropping and recreating all tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print(" Database reset completed.")