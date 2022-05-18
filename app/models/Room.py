from typing import Optional
from pydantic import BaseModel


class Room(BaseModel):
    name: str
    alias: str
    description: Optional[str] = None