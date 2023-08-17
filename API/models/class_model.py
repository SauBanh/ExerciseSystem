from .base import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean
# from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.orm import relationship

class DbClass(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(255))
    class_code = Column(Integer)
    created_at = Column(DateTime())
    status = Column(Boolean, default=True)