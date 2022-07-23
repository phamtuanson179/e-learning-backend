import numbers
from typing import Optional, List
from app.constants.common import QUESTION_TYPE
from pydantic import BaseModel

from app.models.Answer import Answer

# class Answer(BaseModel):
#     content: str
#     is_correct: bool
#     url_file: Optional[str] = None

class QuestionCreate(BaseModel):
    title: str
    subject_id: str
    url_file: Optional[str] = None
    type: str = QUESTION_TYPE.ONE_CORRECT_ANSWER
    answers: List[Answer]

class Question(QuestionCreate):
    id: str

class QuestionHaveAnswer(Question):
    user_answers: List[int]


