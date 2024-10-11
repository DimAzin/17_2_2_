from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base
from user import User
from sqlalchemy.schema import CreateTable

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    # Связь с пользователями
    user = relationship('User', back_populates='tasks')

print(CreateTable(Task.__table__))