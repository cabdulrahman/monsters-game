from base import Base, engine
import models
# Create all tables
Base.metadata.create_all(engine)

print("All tables created successfully.")
