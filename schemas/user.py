# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=too-few-public-methods
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    username: str
    password: str
    email: str
