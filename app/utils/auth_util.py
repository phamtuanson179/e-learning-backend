import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.constants.type import AUTH

class AuthUtil:

    # config for hash password 
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    reusable_oauth2 = HTTPBearer(scheme_name='Authorization')

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(plain_password, hashed_password):
        # return AuthUtil.pwd_context.verify(plain_password, hashed_password)
        return plain_password == hashed_password

    def hash_password(password):
        return AuthUtil.pwd_context.hash(password)

    def create_access_token(username:str)->str:
        expires_delta = timedelta(minutes=AUTH.EXPIRE_MINUTES)
        expire_at = datetime.utcnow()+ expires_delta
        for_encode = {
            'username': username,
            'exp': expire_at
        } 
        encode_jwt = jwt.encode(for_encode, key = AUTH.SECRET_KEY, algorithm = AUTH.ALGORITHM)
        return encode_jwt

    def decode_token(token: str):
        payload = jwt.decode(token, AUTH.SECRET_KEY, algorithms=AUTH.ALGORITHM)
        username: str = payload.get("username")
        exp = payload.get("exp")
        data = {"username": username, "exp": exp}
        return data



