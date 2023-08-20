from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from models.user_model import DbUser

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        user_name = request.user_name,
        email = request.email,
        password = request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    return new_user

def get_all(db: Session):
    return db.query(DbUser).all()