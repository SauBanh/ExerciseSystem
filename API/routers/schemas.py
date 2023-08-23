from pydantic import BaseModel

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

# Class

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