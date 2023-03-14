from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:

    @classmethod
    def bcrypt(cls, plain_password):
        return pwd_cxt.hash(plain_password)

    @classmethod
    def verify(cls, plain_password, hashed_password):
        return pwd_cxt.verify(plain_password, hashed_password)
