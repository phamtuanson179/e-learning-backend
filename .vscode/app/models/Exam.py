from typing import Optional, List
from pydantic import BaseModel
from app.models.Question import Question


class NewExam(BaseModel):
    name: str
    min_point_to_pass: int
    duration: int
    image: Optional[str] = None
    require_rooms: List[str]
    questions: List[Question]

class Exam(NewExam):
    id: Optional[str] = None
    created_by: Optional[str] = None
