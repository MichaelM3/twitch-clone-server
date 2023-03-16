from .database import engine, Base
from .models import relationships

Base.metadata.create_all(bind=engine)
