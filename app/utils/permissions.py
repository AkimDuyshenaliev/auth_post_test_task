from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

from sqlalchemy.orm import query

from app.utils.auth import Auth
from app.utils.user import get_user
from app.db import get_db, Session

security = HTTPBearer()
auth = Auth()


def get_current_user(
        db: Session = Depends(get_db),
        credentials: HTTPAuthorizationCredentials = Depends(security)):
    login = auth.decode_token(credentials.credentials)
    user = get_user(db=db, login=login)
    if not user:
        raise HTTPException(status_code=402, detail="Unauthorized")
    return user

