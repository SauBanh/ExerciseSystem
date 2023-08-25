from sqlalchemy.orm.session import Session
from routers.schemas import ClassBase
from services import user_service, teacher_service, admin_service
from models.class_model import DbClass
from utils.generate import generate_unique_class_code
from fastapi import HTTPException, status

def create_class(db: Session, request: ClassBase, current_user):
    user = user_service.get_user_by_email(db, current_user.email)
    is_teacher = teacher_service.check_teacher(user)
    if not is_teacher:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You do not have access")
    class_codes = [result[0] for result in db.query(DbClass.class_code).all()]
    new_class = DbClass(
        class_name = request.class_name,
        class_code = generate_unique_class_code(class_codes),
        creator_id = user.id
    )
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_all_class(db: Session, current_user):
    is_admin = admin_service.check_admin(current_user)
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You do not have access")
    return db.query(DbClass).all()