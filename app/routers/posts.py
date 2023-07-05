from fastapi import APIRouter, Depends, Security

from app.db import get_db, Session
from app.models.user import User
from app.models.post import Post
from app.schemas.post import GetPost, PostBase, EditPost

from app.utils.permissions import get_current_user
from app.utils.posts import getPosts, createPost, editPost, deletePosts


posts_router = APIRouter(
    tags=['Posts'],
    prefix='/post'
)


@posts_router.get('/get', response_model=GetPost)
def routerGetPosts(id: int, db: Session=Depends(get_db)):
    return getPosts(id=id, db=db)


@posts_router.post('/create', status_code=201)
def routerCreatePost(
    data: PostBase, 
    db: Session=Depends(get_db), 
    user: User=Security(get_current_user)):
    return createPost(data=data, db=db, user=user)


@posts_router.put('/edit', status_code=200)
def routerEditPost(
    id: int, 
    data: EditPost, 
    db: Session=Depends(get_db), 
    user: User=Security(get_current_user)):
    return editPost(id=id, data=data, db=db, user=user)


@posts_router.delete('/delete', status_code=200)
def routerDeletePosts(
    id: int, 
    db: Session=Depends(get_db), 
    user: User=Security(get_current_user)):
    return deletePosts(id=id, db=db, user=user)