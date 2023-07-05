from fastapi import FastAPI
from app.db import engine, Base

from fastapi.middleware.cors import CORSMiddleware

from app.models.user import User
from app.models.post import Post
from app.models.reaction import Reaction

from app.routers.auth import auth_router
from app.routers.posts import posts_router
from app.routers.reactions import reaction_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(posts_router)
app.include_router(reaction_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
