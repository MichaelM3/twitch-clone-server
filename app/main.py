from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import models
from .db.database import engine
from .routes import user, auth
from . import config

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@lru_cache()
def get_settings():
    return config.settings

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def index():
    return "Home page"
