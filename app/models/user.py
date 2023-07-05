from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db import Base
from app.models.post import Post


class User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    posts = relationship(
        "Post", 
        back_populates="author", 
        cascade="all, delete-orphan")