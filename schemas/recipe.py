# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from typing import Optional
from pydantic import BaseModel


class Recipe(BaseModel):
    recipe_id: Optional[int]
    name: str
    servings: Optional[int]
    time_preparation_h: Optional[int]
    time_preparation_m: Optional[int]
    difficulty: Optional[int]
    is_public: Optional[str]
    ingredients: Optional[str]
    description: Optional[str]
