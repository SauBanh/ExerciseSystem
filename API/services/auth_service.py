# Trong file auth_service, tạo các hàm như authenticate_user, create_session, verify_token, và encrypt_data.
# from sqlalchemy.orm.session import Session
from utils.hashing import Hash
from fastapi import HTTPException, status#, Depends
from services.user_service import get_current_user
from utils.token import create_access_token, decode_access_token
# from database.database import get_db


def login(request, db):
    user = get_current_user(db, username=request.username)
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    
    # Tạo mã thông báo xác thực (authentication token) và trả về
    access_token = create_access_token(data={
        'user_name': user.user_name,
        'user_id': user.id,
        'email': user.email,
        'role_id': user.role_id,
    })
    
    return {
        "access_token": access_token, 
        "token_type": "Bearer",
    }

def decode_user_token(token: str):
    decoded_token = decode_access_token(token)
    if decoded_token:
        user_name = decoded_token.get("user_name")
        user_id = decoded_token.get("user_id")
        email = decoded_token.get("email")
        role_id = decoded_token.get("role_id")
    
        if user_name and email and role_id:
            return {
                'user_name': user_name,
                'id': user_id,
                'email': email,
                'role_id': role_id
            }
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token không chứa đủ thông tin cần thiết.")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token không hợp lệ hoặc đã hết hạn.")