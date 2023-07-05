from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    login: str

    class Config:
        orm_mode = True


class SignIn(BaseModel):
    login: str
    password: str


class SignUp(SignIn):
    first_name: str | None = None
    last_name: str | None = None


class Token(BaseModel):
    token: str