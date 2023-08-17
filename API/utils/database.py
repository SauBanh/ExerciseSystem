from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.exc import SQLAlchemyError
from models.class_model import DbClass
from models.user_model import DbUser


load_dotenv()
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
# secret_key = os.getenv("SECRET_KEY")
# debug = os.getenv("DEBUG")


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./ig_api.db'
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/exercise_system"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:0962147976@:3306/exercise_system"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # Kiểm tra kết nối
    engine.connect()
    print("Kết nối thành công đến cơ sở dữ liệu.")
except SQLAlchemyError as e:
    print("Lỗi kết nối đến cơ sở dữ liệu:", str(e))

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

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