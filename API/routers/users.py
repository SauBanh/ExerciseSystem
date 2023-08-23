from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_db
from routers.schemas import UserDisplay, UserAuth, PasswordBase
from services import user_service
from utils.token import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get('', response_model=UserDisplay, status_code=status.HTTP_200_OK)
def get_user(current_user: UserAuth = Depends(get_current_user)):
    return current_user

@router.put('/change_password', status_code=status.HTTP_204_NO_CONTENT)
def change_password(request: PasswordBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return user_service.change_password(db, request, current_user)