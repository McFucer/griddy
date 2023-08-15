from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:papa@localhost:5432/twitter"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()