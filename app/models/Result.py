from typing import List, Optional
from pydantic import BaseModel
from app.models.question import Question, QuestionResponse

from app.models.subject import Subject
from app.models.user import User


class ResultCreate(BaseModel):
    subject: Subject
    point: int
    is_pass: bool
    time: int
    user: User
    questions: List[Question]


class Result(ResultCreate):
    id: Optional[str] = None
    max_point: int
    create_at: str

