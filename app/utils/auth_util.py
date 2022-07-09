from unittest import result
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer

from app.configs.Config import AuthConfig

class AuthUtil:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    reusable_oauth2 = HTTPBearer(scheme_name='Authorization')

    def verify_password(plain_password, hashed_password):
        return AuthUtil.pwd_context.verify(plain_password, hashed_password)
        # return True

    def hash_password(password):
        return AuthUtil.pwd_context.hash(password)

    def create_access_token(username: str) -> str:
        expires_delta = timedelta(minutes=AuthConfig.EXPIRE_MINUTES)
        expires_at = datetime.utcnow() + expires_delta
        to_encode = {
            "username": username, 
            "exp": expires_at
            }
        encoded_jwt = jwt.encode(to_encode, key=AuthConfig.SECRET_KEY, algorithm=AuthConfig.ALGORITHM)
        return encoded_jwt

    def decode_token(token: str):
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        username = payload.get("username")
        exp = payload.get("exp")
        return {"username": username, "exp": exp}