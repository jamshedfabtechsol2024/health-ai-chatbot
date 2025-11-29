from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Updated database credentials
DATABASE_URL = (
    "postgresql://postgres:8aIEmZTmyOCxkEOWE6YL@"
    "database-1.c34qk000ky28.eu-north-1.rds.amazonaws.com:5432/postgres"
)

# Create the synchronous engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
