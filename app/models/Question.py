from typing import Optional, List
from pydantic import BaseModel

from app.models.Answer import Answer

class Question(BaseModel):
    type: int
    content: str
    url_file: Optional[str] = None
    answers: List[Answer]
