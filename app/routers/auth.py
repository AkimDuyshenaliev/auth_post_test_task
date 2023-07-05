from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from app.utils.auth import Auth
from app.schemas.auth import SignIn, SignUp, UserBase, Token
from app.db import Session, get_db
from app.utils.user import get_user, create_user


auth_handler = Auth()
auth_router = APIRouter(
    tags=['Authorization'],
    prefix='/auth'
)


@auth_router.post('/signup', response_model=UserBase)
def signup(user: SignUp, db: Session=Depends(get_db)):
    return create_user(db=db, user=user)


@auth_router.post('/signin', response_model=Token)
def signin(user: SignIn, db: Session=Depends(get_db)):
    db_user = get_user(db=db, login=user.login)

    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid login")
    if not auth_handler.verify_password(password=user.password, encoded_password=db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"token": auth_handler.encode_token(username=db_user.login)}