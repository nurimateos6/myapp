from pydantic import BaseModel
from typing import Optional
from sqlalchemy.sql.sqltypes import DateTime


class User(BaseModel):
        id: Optional[int]
        username: str
        password: str
        email: str


