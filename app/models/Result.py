from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from app.models.Question import Question, QuestionHaveAnswer


class ResultCreate(BaseModel):
    created_at:Optional[int] 
    subject_id: str 
    point: int
    is_pass: bool
    time: int
    user_id: str
    questions: List[QuestionHaveAnswer]


class Result(ResultCreate):
    id: Optional[str] = None

