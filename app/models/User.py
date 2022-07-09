from typing import List, Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password: str
    email: str
    role: str
    fullname: str
    dob: str
    list_subjects_id: Optional[List[str]]
    avatar: Optional[str] 
    token: Optional[str] = None

class User(UserCreate):
    id: str
