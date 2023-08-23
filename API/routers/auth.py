from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends
from database.database import get_db
from routers.schemas import UserDisplay
from services import auth_service, user_service
from routers.schemas import Token, UserBase
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user_service.create_user(db, request)

@router.post('/token', response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_service.login(request, db)

# @router.post('/user', response_model=UserDisplay)
# def get_current_user(token: TokenRequest):
#     user = auth_service.decode_user_token(token.token)
#     return user