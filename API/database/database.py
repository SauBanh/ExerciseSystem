from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.class_model import DbClass
from models.user_model import DbUser
from configs.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    DbUser.metadata.create_all(bind=engine)
    DbClass.metadata.create_all(bind=engine)