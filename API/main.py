from fastapi import FastAPI
from database.database import create_tables
from tests.test_connect_db import check_connection_db
from routers import users


check_connection_db()

create_tables()

app=FastAPI()

app.include_router(users.router)

@app.get('/')
def root():
    return "hello world"