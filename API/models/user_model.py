from .base import Base
from sqlalchemy import Column, String, Integer, Boolean
# from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    role = Column(Integer)
    status = Column(Boolean, default=True)