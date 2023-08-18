from configs.config import SQLALCHEMY_DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def check_connection_db():
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        # Kiểm tra kết nối
        engine.connect()
        print("Successful connection to the database.")
    except SQLAlchemyError as e:
        print("Error connecting to database:", str(e))