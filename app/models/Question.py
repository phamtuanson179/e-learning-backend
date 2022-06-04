from typing import Optional, List
from pydantic import BaseModel
from app.models.subject import Subject


class Answer(BaseModel):
    content: str
    is_correct: bool
    url_file: Optional[str] = None

class QuestionCreate(BaseModel):
    type: int
    title: str
    subject: Subject
    url_file: Optional[str] = None
    answers: List[Answer]

class Question(QuestionCreate):
    id: str
class QuestionResponse(QuestionCreate):
    pass








