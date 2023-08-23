from .base import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class DbAnswer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
    content = Column(String(255), nullable=False)
    is_correct = Column(Boolean, nullable=False)

    # Tạo quan hệ từ 'question' trong bảng 'DbQuestion' về 'answers' trong bảng này
    question = relationship("DbQuestion", back_populates="answers")
    # Thiết lập mối quan hệ 1-nhiều với bảng DbAnswerSession (bởi anwser_id)
    answer_sessions = relationship("DbAnswerSession", back_populates="answers")