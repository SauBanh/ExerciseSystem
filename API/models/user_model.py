from .base import Base
from sqlalchemy import ForeignKey, Column, String, Integer, Boolean, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255))
    role_id = Column(Integer, ForeignKey('role.id'), default=1)
    email = Column(String(255))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    create_at = Column(DateTime, default=datetime.utcnow)

    # Thiết lập mối quan hệ 1-nhiều với bảng DbRole
    role = relationship("DbRole", back_populates="users")
    # Thiết lập mối quan hệ 1-nhiều với bảng DbClassMember
    class_memberships = relationship("DbClassMember", back_populates="user")
    # Thiết lập mối quan hệ 1-nhiều với bảng DbAssignment (bởi creator_id)
    created_assignments = relationship("DbAssignment", back_populates="user")
    # Thiết lập mối quan hệ 1-nhiều với bảng DbAnswerSession (bởi user_id)
    answer_sessions = relationship("DbAnswerSession", back_populates="user")