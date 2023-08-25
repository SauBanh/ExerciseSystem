from pydantic import BaseModel
from datetime import datetime

# User

class UserBase(BaseModel):
    user_name: str
    email: str
    password: str
    first_name: str
    last_name: str

class UserDisplay(BaseModel):
    user_name: str
    id: int
    email: str
    role_id: int
    first_name: str
    last_name: str
    class Config():
        from_attributes = True

# Auth

class LoginBase(BaseModel):
    user_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenRequest(BaseModel):
    token: str

class UserAuth(BaseModel):
    user_name: str
    id: int
    email: str
    role_id: int

class PasswordBase(BaseModel):
    password: str
    new_password: str

# Class

class ClassBase(BaseModel):
    class_name: str

class ClassDisabled(BaseModel):
    class_name: str
    class_code: str

class ClassRoom(BaseModel):
    class_name: str
    class_code: str
    is_active: bool
    id: int
    creator_id: int
    created_at: datetime

# class ClassMemberBase(BaseModel):
