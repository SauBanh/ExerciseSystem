from .base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class DbRole(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    # Tạo quan hệ ngược từ bảng 'role' đến 'user'
    users = relationship("DbUser", back_populates="role")