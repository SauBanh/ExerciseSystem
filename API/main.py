from fastapi import FastAPI
from utils.database import create_tables

create_tables()

app = FastAPI()

@app.get('/')
def root():
    return "hello world"