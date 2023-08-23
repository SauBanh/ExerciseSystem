from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from models.user_model import DbUser
from utils.hashing import Hash
from fastapi import HTTPException, status
from routers.schemas import PasswordBase

def create_user(db: Session, request: UserBase):

    user_exist = db.query(DbUser).filter(DbUser.user_name == request.user_name).first()
    email_exist = db.query(DbUser).filter(DbUser.email == request.email).first()

    if user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Tên tài khoản {request.user_name} đã tồn tại. Vui lòng chọn tên khác.")
    
    if email_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Email {request.email} đã tồn tại.")

    new_user = DbUser(
        user_name = request.user_name,
        email = request.email,
        password = Hash.bcrypt(request.password),
        first_name = request.first_name,
        last_name = request.last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_current_user(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.user_name == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with username {username} not found')
    return user

def get_user_by_email(db: Session, email: str):
    user = db.query(DbUser).filter(DbUser.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_200_OK,detail=f'User with username {email} not found')
    return user

def get_all(db: Session):
    return db.query(DbUser).all()

# def get_user_by_username(db: Session, username: str):
#     user = db.query(DbUser).filter(DbUser.user_name == username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with username {username} not found')
#     return user

def verify_password(db_password, user_input_password):    
    if not Hash.verify(db_password, user_input_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    return True

def change_password(db: Session, request: PasswordBase, current_user):
    user = get_user_by_email(db, current_user.email)
    is_correct_password = verify_password(user.password, request.password)
    if not is_correct_password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    user.password = Hash.bcrypt(request.new_password)
    db.add(user)
    db.commit()