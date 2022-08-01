from typing import Optional
from pydantic import BaseModel

from app.constants.common import GENERATE_EXAM_TYPE


class SubjectUpdate(BaseModel):
    name: str
    alias: str
    description: Optional[str] = None
    time: int
    amount_question: int
    min_correct_question_to_pass: int
    

class SubjectCreate(SubjectUpdate):
    image:str


class Subject(SubjectCreate):
    id: str
