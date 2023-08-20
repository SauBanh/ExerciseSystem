from .base import Base
from sqlalchemy import Column, DateTime, Integer, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class DbClassMember(Base):
    __tablename__ = 'class_member'
    id = Column(Integer, primary_key=True, index=True)
    join_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    class_id = Column(Integer, ForeignKey('class.id', ondelete='CASCADE'))
    
    # Tạo quan hệ từ 'class_memberships' trong bảng 'DbUser' về 'user' trong bảng này
    user = relationship("DbUser", back_populates="class_memberships")
    # Tạo quan hệ từ 'class_members' trong bảng 'DbClass' về 'db_class' trong bảng này
    classDb = relationship("DbClass", back_populates="class_members")