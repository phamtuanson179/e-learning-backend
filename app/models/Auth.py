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
    curr_password: str
    new_password: str
    confirm_password: str