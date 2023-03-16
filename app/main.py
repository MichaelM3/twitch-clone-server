from functools import lru_cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user_route, auth_route
from . import config

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

app.include_router(user_route.router)
app.include_router(auth_route.router)

@app.get("/")
def index():
    return "Home page"
