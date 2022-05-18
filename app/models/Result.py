from typing import Optional
from pydantic import BaseModel


class NewResult(BaseModel):
    exam_id: str
    point: int
    is_pass: bool
    duration: int

class Result(NewResult):
    id: Optional[str] = None
    user_name: str
    user_id: str
    max_point: int

class FullResult(Result):
    create_at: str