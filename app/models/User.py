from typing import List, Optional

from app.models.subject import Subject
from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password: str
    email: str
    subject: Optional[List[Subject]]
    role: int
    fullname: str
    dob: str
    url_avatar: Optional[str] 
    token: Optional[str] = None

class UserResponse(UserCreate): 
    id: str
class User(UserResponse):
    pass
