from typing import Optional, List
from pydantic import BaseModel
from app.models.Subject import Subject


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

class QuestionResponse(QuestionCreate):
    id: str

class Question(QuestionResponse):
    pass

class ExamCreate(BaseModel):
    subject: Subject
    min_point_to_pass: int
    time: int
    questions: List[Question]
    code: str

class Exam(ExamCreate):
    id: Optional[str] = None
    created_by: Optional[str] = None





