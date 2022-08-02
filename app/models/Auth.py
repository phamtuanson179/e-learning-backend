from typing import Optional
from pydantic import BaseModel


class Account(BaseModel):
    email: str
    password: Optional[str] = None

class AccessToken(BaseModel):
    username: str
    token: str
    role: str

class ForgotPassword(BaseModel):
    email: str

class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    repeat_new_password: str