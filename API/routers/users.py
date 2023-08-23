from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_db
from routers.schemas import UserDisplay, UserAuth
from services import user_service, admin_service
from typing import List
from utils.token import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get('', response_model=UserDisplay)
def get_user(current_user: UserAuth = Depends(get_current_user)):
    return current_user

@router.get('/all', response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    is_admin = admin_service.check_admin(current_user)
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You do not have access")
    return user_service.get_all(db)