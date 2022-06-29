from typing import Optional, List
from pydantic import BaseModel, Field
from app.models.Subject import SubjectCreate
from app.models.PyObjectId import PyObjectId
from bson import ObjectId

class Answer(BaseModel):
    content: str
    is_correct: bool
    url_file: Optional[str] = None

class QuestionCreate(BaseModel):
    type: int
    title: str
    subject: SubjectCreate
    url_file: Optional[str] = None
    answers: List[Answer]

class Question(QuestionCreate):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = {
            
        # }
class QuestionResponse(QuestionCreate):
    pass








