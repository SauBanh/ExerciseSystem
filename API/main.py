from fastapi import FastAPI
from database.database import create_tables
from tests.test_connect_db import check_connection_db
from routers import users, auth, admin, teacher, class_room


check_connection_db()

create_tables()

app=FastAPI(title='API Exercises System')

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(teacher.router)
app.include_router(class_room.router)
app.include_router(admin.router)

@app.get('/')
def root():
    return "hello world"
