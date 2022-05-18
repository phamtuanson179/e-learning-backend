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

    def hash_password(password):
        return AuthUtil.pwd_context.hash(password)

    def create_access_token(email: str) -> str:
        expires_delta = timedelta(minutes=AuthConfig.EXPIRE_MINUTES)
        expires_at = datetime.utcnow() + expires_delta
        to_encode = {
            "email": email, 
            "exp": expires_at
            }
        encoded_jwt = jwt.encode(to_encode, key=AuthConfig.SECRET_KEY, algorithm=AuthConfig.ALGORITHM)
        return encoded_jwt

    def decode_token(token: str):
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        email: str = payload.get("email")
        exp = payload.get("exp")
        data = {"email": email, "exp": exp}
        return data