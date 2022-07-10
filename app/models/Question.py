from typing import Optional, List
from pydantic import BaseModel

from app.models.Answer import Answer

# class Answer(BaseModel):
#     content: str
#     is_correct: bool
#     url_file: Optional[str] = None

class QuestionCreate(BaseModel):
    type: int
    title: str
    subject_id: str
    url_file: Optional[str] = None
    answers: List[Answer]

class Question(QuestionCreate):
    id: str



