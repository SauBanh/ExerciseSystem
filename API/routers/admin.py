from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_db
from routers.schemas import UserDisplay
from services import admin_service
from routers.schemas import UserBase, UserAuth
from utils.token import get_current_user

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