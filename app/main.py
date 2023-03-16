from functools import lru_cache
from fastapi import FastAPI
from .routes import user_route, auth_route
from .config import config, cors

app = FastAPI()

cors.setup_cors(app)

@lru_cache()
def get_settings():
    return config.settings

app.include_router(user_route.router)
app.include_router(auth_route.router)
