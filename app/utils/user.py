from app.db import Session, save_object
from sqlalchemy.orm import query
from fastapi import HTTPException

from app.schemas.auth import UserBase, SignUp

from app.utils.auth import Auth
from app.models.user import User


auth_handler = Auth()


def get_user(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()


def create_user(db: Session, user: SignUp):
    if get_user(db=db, login=user.login):
        raise HTTPException(status_code=400, detail='Login already taken')

    hashed_password = auth_handler.encode_password(user.password)
    db_user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        login = user.login,
        password = hashed_password
    )
    return save_object(object=db_user, db=db)