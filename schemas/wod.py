from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Wod(BaseModel):
    wod_id: Optional[int]
    name: str
    persons: Optional[int]
    time_wod_h: Optional[int]
    time_wod_m: Optional[int]
    difficulty: Optional[int]
    is_public: Optional[bool]
    materials: Optional[str]
    description: Optional[str]
    creation_date: Optional[datetime]
