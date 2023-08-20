from .base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class DbQuestion(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey('assignment.id'))
    title = Column(String(255))
    content = Column(String(255))

    # Tạo quan hệ từ 'assignment' trong bảng 'DbAssignment' về 'assignment_questions' trong bảng này
    assignment = relationship("DbAssignment", back_populates="questions")
    # Tạo quan hệ 1-nhiều với bảng DbAnswer (bởi question_id)
    answers = relationship("DbAnswer", back_populates="question")
    # Tạo quan hệ 1-nhiều với bảng DbAnswerSession (bởi question_id)
    answer_sessions = relationship("DbAnswerSession", back_populates="question")