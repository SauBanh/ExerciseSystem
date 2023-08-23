from .base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class DbAnswerSession(Base):
    __tablename__ = 'answer_session'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
    anwser_id = Column(Integer, ForeignKey('answer.id'), nullable=False)

    # Tạo quan hệ từ 'question' trong bảng 'DbQuestion' về 'answer_sessions' trong bảng này
    question = relationship("DbQuestion", back_populates="answer_sessions")
    # Tạo quan hệ từ 'user' trong bảng 'DbUser' về 'answer_sessions' trong bảng này
    user = relationship("DbUser", back_populates="answer_sessions")
    # Tạo quan hệ từ 'answer' trong bảng 'DbAnswer' về 'answer_sessions' trong bảng này
    answers = relationship("DbAnswer", back_populates="answer_sessions")