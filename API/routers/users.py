from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from database.database import get_db
from .schemas import UserDisplay, UserBase
from services import user_service
from typing import List
router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user_service.create_user(db, request)

@router.get('/all', response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
    return user_service.get_all(db)