import email
from typing import Optional

from pydantic import BaseModel

class Account(BaseModel):
    email: str
    password: Optional[str] = None

class User(Account):
    user_id: Optional[str] = None
    role: Optional[int] = None
    room: str
    fullname: str
    position: str
    date_of_birth: Optional[str] = None
    url_avatar: Optional[str] = None
    token: Optional[str] = None

class NewUser(BaseModel):
    email: str
    password: str
    room: str
    role: int
    fullname: str
    position: str

class AccessToken(BaseModel):
    email: str
    token: str

class ForgotPassword(BaseModel):
    email: str

class ChangePassword(BaseModel):
    curr_password: str
    new_password: str
    confirm_password: str