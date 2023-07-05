from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db import Base


class Reaction(Base):
    __tablename__='reaction'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    post_id = Column(ForeignKey("post.id"), nullable=False)
    reaction = Column(Boolean, nullable=False) # True - like, False - dislike