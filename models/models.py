from datetime import datetime 
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from db import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)