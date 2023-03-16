from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(plain_password):
    return pwd_cxt.hash(plain_password)

def verify(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)
