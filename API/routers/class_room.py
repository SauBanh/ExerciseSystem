from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, status
from database.database import get_db
from routers.schemas import UserAuth, ClassDisabled, ClassBase
from utils.token import get_current_user
from services import class_service
from typing import List

router = APIRouter(
    prefix="/class",
    tags=['class']
)

@router.post('', response_model=ClassDisabled, status_code=status.HTTP_201_CREATED)
def create_class(request: ClassBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return class_service.create_class(db, request, current_user)