from typing import Optional
from pydantic import BaseModel

from app.constants.type import GENERATE_EXAM_TYPE


class SubjectCreate(BaseModel):
    name: str
    alias: str
    description: Optional[str] = None
    time: int
    amount_question: int
    min_correct_question_to_pass: int
    generate_exam_type: str = GENERATE_EXAM_TYPE.ORDER

class Subject(SubjectCreate):
    id: str