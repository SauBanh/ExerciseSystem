from .base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class DbAssignment(Base):
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    title = Column(String(255))
    description = Column(String(255), nullable=True) # Đặt nullable=True để cho phép cột này có thể rỗng
    deadline = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(255))

    # Tạo quan hệ từ 'created_assignments' trong bảng 'DbUser' về 'creator' trong bảng này
    user = relationship("DbUser", back_populates="created_assignments")
    # Tạo quan hệ từ 'class_assignments' trong bảng 'DbClass' về 'assignments' trong bảng này
    classDb = relationship("DbClass", back_populates="assignments")
    # Tạo quan hệ từ 'assignment_questions' trong bảng 'DbQuestion' về 'assignment' trong bảng này
    questions = relationship("DbQuestion", back_populates="assignment")