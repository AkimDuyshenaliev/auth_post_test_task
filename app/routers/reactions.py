from fastapi import APIRouter, Depends, Security

from app.db import get_db, Session
from app.models.user import User

from app.utils.permissions import get_current_user

from app.utils.reactions import postLikeDislike


reaction_router = APIRouter(
    tags=['Reactions'],
    prefix='/reaction'
)


@reaction_router.post('', status_code=201)
def routerPostLikeDislike(
        post_id: int,
        reaction: bool,
        db: Session = Depends(get_db),
        user: User = Security(get_current_user)):
    '''
    True = Like\n
    False = Dislike
    '''
    return postLikeDislike(post_id=post_id, reaction=reaction, db=db, user=user)
