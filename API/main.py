from fastapi import FastAPI
from database.database import create_tables
from tests.test_connect_db import check_connection_db

check_connection_db()

create_tables()

app = FastAPI()

@app.get('/')
def root():
    return "hello world"