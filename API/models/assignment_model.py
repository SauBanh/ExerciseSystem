from .base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

class DbAssignment(Base):
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    class_id = Column(Integer, ForeignKey('class.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True) # Đặt nullable=True để cho phép cột này có thể rỗng
    deadline = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Tạo quan hệ từ 'created_assignments' trong bảng 'DbUser' về 'creator' trong bảng này
    user = relationship("DbUser", back_populates="created_assignments")
    # Tạo quan hệ từ 'class_assignments' trong bảng 'DbClass' về 'assignments' trong bảng này
    classDb = relationship("DbClass", back_populates="assignments")
    # Tạo quan hệ từ 'assignment_questions' trong bảng 'DbQuestion' về 'assignment' trong bảng này
    questions = relationship("DbQuestion", back_populates="assignment")