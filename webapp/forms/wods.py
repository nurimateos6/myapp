from typing import List, Optional
from fastapi import Request
from webapp.forms.utils import is_valid


class WodsForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.wod_id: int = None
        self.name: Optional[str] = None
        self.persons: Optional[int] = None
        self.time_wod_h: Optional[int] = None
        self.time_wod_m: Optional[int] = None
        self.difficulty: Optional[int] = None
        self.is_public: Optional[bool] = None
        self.materials: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.wod_id = form.get("wod_id")
        self.name = form.get("name")
        self.persons = form.get("persons")
        self.time_wod_h = form.get("time_wod_h")
        self.time_wod_m = form.get("time_wod_m")
        self.difficulty = form.get("difficulty")
        self.is_public = form.get("is_public")
        self.materials = form.get("materials")
        self.description = form.get("description")
        is_valid()
