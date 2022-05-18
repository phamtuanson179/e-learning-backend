from typing import Optional
from pydantic import BaseModel


class Answer(BaseModel):
    content: str
    is_correct: bool
    url_file: Optional[str] = None
