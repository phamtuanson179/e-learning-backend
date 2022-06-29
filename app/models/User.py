from typing import List, Optional

from app.models.Subject import SubjectCreate
from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password: str
    email: str
    role: str
    fullname: str
    dob: str
    subjects: Optional[List[SubjectCreate]]
    url_avatar: Optional[str] 
    token: Optional[str] = None

class UserResponse(UserCreate): 
    id: str
class User(UserResponse):
    pass
