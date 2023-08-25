from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from database.database import get_db
from routers.schemas import UserDisplay, UserAuth
from utils.token import get_current_user
from services import teacher_service
from routers.schemas import UserBase, ClassRoom
from typing import List

router = APIRouter(
    prefix="/teacher",
    tags=['teacher']
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return teacher_service.create_account_teacher(db, request)

@router.get('/classrooms', response_model=List[ClassRoom])
def get_all_class(db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return teacher_service.get_all_class_of_teacher(db, current_user)