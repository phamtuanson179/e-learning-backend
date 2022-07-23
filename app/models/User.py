from typing import List, Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password: Optional[str]
    email: str
    role: str
    fullname: str
    dob: int
    list_subjects_id: Optional[List[str]]
    avatar: Optional[str] 
    token: Optional[str]

class User(UserCreate):
    id: str
