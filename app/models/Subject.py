from typing import Optional
from pydantic import BaseModel


class SubjectCreate(BaseModel):
    name: str
    alias: str
    description: Optional[str] = None
   


class Subject(SubjectCreate):
    id: str