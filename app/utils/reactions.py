from fastapi.exceptions import HTTPException

from app.db import Session, save_object
from app.models.user import User
from app.models.reaction import Reaction

from app.models.post import Post

from sqlalchemy import and_


def postLikeDislike(post_id: int, reaction: bool, db: Session, user: User):
    post = db.query(Post).filter(Post.id==post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id == user.id:
        raise HTTPException(status_code=403, detail="Can't like/dislike your own posts")

    db_reaction = db.query(Reaction).filter(and_(
        Reaction.post_id==post_id, 
        Reaction.user_id==user.id)).first()

    if db_reaction:
        setattr(db_reaction, 'reaction', reaction)
        return save_object(db=db, object=db_reaction)

    db_reaction = Reaction(
        user_id = user.id,
        post_id = post.id,
        reaction = reaction
    )
    return save_object(db=db, object=db_reaction)
    
    