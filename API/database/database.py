from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import DbUser
from models.role_model import DbRole
from models.class_model import DbClass
from models.answer_model import DbAnswer
from models.answer_sesstion_model import DbAnswerSession
from models.assignment_model import DbAssignment
from models.class_member_model import DbClassMember
from models.question_model import DbQuestion
from configs.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    DbUser.metadata.create_all(bind=engine)
    DbRole.metadata.create_all(bind=engine)
    DbClass.metadata.create_all(bind=engine)
    DbAnswer.metadata.create_all(bind=engine)
    DbAnswerSession.metadata.create_all(bind=engine)
    DbAssignment.metadata.create_all(bind=engine)
    DbClassMember.metadata.create_all(bind=engine)
    DbQuestion.metadata.create_all(bind=engine)