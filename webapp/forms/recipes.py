from typing import List, Optional
from fastapi import Request
from webapp.forms.utils import is_valid



class RecipesForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.servings: Optional[int] = None
        self.time_preparation_h: Optional[int] = None
        self.time_preparation_m: Optional[int] = None
        self.difficulty: Optional[int] = None
        self.is_public: Optional[bool] = None
        self.ingredients: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.servings = form.get("servings")
        self.time_preparation_h = form.get("time_preparation_h")
        self.time_preparation_m = form.get("time_preparation_m")
        self.difficulty = form.get("difficulty")
        self.is_public = form.get("is_public")
        self.ingredients = form.get("ingredients")
        self.description = form.get("description")
        is_valid()

