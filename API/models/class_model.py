from .base import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

# from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.orm import relationship

class DbClass(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(255))
    class_code = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Thiết lập mối quan hệ 1-nhiều với bảng DbClassMember
    class_members = relationship("DbClassMember", back_populates="classDb")
    # Thiết lập mối quan hệ 1-nhiều với bảng DbAssignment (bởi class_id)
    assignments = relationship("DbAssignment", back_populates="classDb")