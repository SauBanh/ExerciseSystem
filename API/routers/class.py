from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_db
from routers.schemas import UserDisplay, UserAuth, PasswordBase
from services import user_service
from utils.token import get_current_user

router = APIRouter(
    prefix="/class",
    tags=['class']
)

# @router.post('')
# def create_class()