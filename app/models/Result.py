from typing import List, Optional
from pydantic import BaseModel
from app.models.Question import Question, QuestionResponse

from app.models.Subject import SubjectCreate
from app.models.User import User


class ResultCreate(BaseModel):
    subject: SubjectCreate
    point: int
    is_pass: bool
    time: int
    user: User
    questions: List[Question]


class Result(ResultCreate):
    id: Optional[str] = None
    max_point: int
    create_at: str

