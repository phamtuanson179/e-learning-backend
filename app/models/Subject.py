from typing import Optional
from pydantic import BaseModel

from app.constants.common import GENERATE_EXAM_TYPE


class SubjectCreate(BaseModel):
    name: str
    alias: str
    description: Optional[str] = None
    time: int
    amount_question: int
    min_correct_question_to_pass: int
    image:str

class Subject(SubjectCreate):
    id: str

class SubjectUpdate(SubjectCreate):
   pass