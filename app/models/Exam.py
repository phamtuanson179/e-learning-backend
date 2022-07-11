from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class ExamCreate(BaseModel):
    tenBaiKT: str
    description: Optional(str)
    timeBegin: str
    timeEnd: str

class Exam(ExamCreate):
    maKT: str
    ngaytao: str
