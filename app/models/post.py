from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db import Base
from app.models.reaction import Reaction


class Post(Base):
    __tablename__='post'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())

    author_id = Column(ForeignKey('user.id'), unique=False, nullable=False)
    author = relationship('User', back_populates="posts")

    reactions = relationship('Reaction', cascade="all, delete-orphan", backref="post")