from pydantic import BaseModel

# User

class UserBase(BaseModel):
    user_name: str
    email: str
    password: str

class UserDisplay(BaseModel):
    user_name: str
    email: str
    class Config():
        from_attributes = True

# Class 