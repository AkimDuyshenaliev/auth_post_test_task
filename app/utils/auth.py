import jwt
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta


class Auth():
    hasher = CryptContext(schemes=['bcrypt'])
    secret = 'e98ae8929541bdb527376159868086b6c0bab9c4687cd6b87436b75fea7c0de8'

    def encode_password(self, password):
        return self.hasher.hash(password)
    
    def verify_password(self, password, encoded_password):
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, username):
        payload = {
            'exp': datetime.utcnow() + timedelta(weeks=1, days=0, hours=0, minutes=0, seconds=0),
            'iat': datetime.utcnow(),
            'scope': 'access_token',
            'sub': username
        }
        return jwt.encode(
            payload=payload,
            key=self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            if (payload['scope'] == 'access_token'):
                return payload['sub']
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')