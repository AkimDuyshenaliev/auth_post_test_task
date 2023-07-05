from fastapi.exceptions import HTTPException

from app.db import Session, save_object
from app.models.user import User
from app.models.post import Post
from app.models.reaction import Reaction

from app.schemas.post import PostBase, EditPost

from sqlalchemy import and_


def getPosts(id: int, db: Session):
    data = db.query(Post).filter(Post.id == id).first()
    data.likes = len([i for i in data.reactions if i.reaction])
    data.dislikes = len([i for i in data.reactions if not i.reaction])
    print(data)
    return data


def createPost(data: PostBase, db: Session, user: User):
    post = Post(
        title = data.title,
        text = data.text,
        author_id = user.id
    )
    return save_object(db=db, object=post)


def editPost(id:int, data: EditPost, db: Session, user: User):
    post = db.query(Post).filter(Post.id==id).first()

    for element in data:
        if element[0] in post.__dict__ and element[1] != None:
            setattr(post, element[0], element[1])

    return save_object(db=db, object=post)
            


def deletePosts(id: int, db: Session, user: User):
    post = db.query(Post).filter(Post.id==id).first()
    if post and post.author_id == user.id:
        db.delete(post)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Post not found")