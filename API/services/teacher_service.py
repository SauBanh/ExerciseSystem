from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from models.user_model import DbUser
from fastapi import HTTPException, status
from utils.hashing import Hash

def create_account_teacher(db: Session, request: UserBase):
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
        last_name = request.last_name,
        role_id = 2
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def check_teacher(current_user):
    if current_user.role_id != 2:
        return False
    return True