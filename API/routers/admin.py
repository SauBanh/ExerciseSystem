from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_db
from routers.schemas import UserDisplay
from services import admin_service, user_service, class_service
from routers.schemas import UserBase, UserAuth, ClassRoom
from utils.token import get_current_user
from typing import List

router = APIRouter(
    prefix="/admin",
    tags=['admin']
)

@router.post('', response_model=UserDisplay)
def create_admin(request: UserBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    is_admin = admin_service.check_admin(current_user)
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You do not have access")
    return admin_service.create_account(db, request)

@router.get('/users', response_model=List[UserDisplay], status_code=status.HTTP_200_OK)
def get_all_user(db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    is_admin = admin_service.check_admin(current_user)
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You do not have access")
    return user_service.get_all(db)

@router.get('/classrooms', response_model=List[ClassRoom])
def get_classrooms(db: Session = Depends(get_db),  current_user: UserAuth = Depends(get_current_user)):
    return class_service.get_all_class(db, current_user)