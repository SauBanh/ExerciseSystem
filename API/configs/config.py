from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
# secret_key = os.getenv("SECRET_KEY")
# debug = os.getenv("DEBUG")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/exercise_system"