from typing import Optional
from pydantic import BaseModel
from app.models.Exam import Exam

from app.models.Subject import Subject
from app.models.User import User


class ResultCreate(BaseModel):
    subject: Subject
    point: int
    is_pass: bool
    time: int
    user: User
    exam: Exam


class Result(ResultCreate):
    id: Optional[str] = None
    max_point: int
    create_at: str

