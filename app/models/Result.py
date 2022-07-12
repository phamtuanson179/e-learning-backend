from typing import List, Optional
from pydantic import BaseModel

from app.models.Question import Question


class ResultCreate(BaseModel):
    subject_id: str 
    point: int
    is_pass: bool
    time: int
    user_id: str
    questions: List[Question]


class Result(ResultCreate):
    # id: Optional[str] = None
    max_point: int
    create_at: str
