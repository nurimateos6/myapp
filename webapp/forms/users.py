from typing import List, Optional
from fastapi import Request
from webapp.forms.utils import is_valid


class UsersForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.user_name: Optional[str] = None
        self.user_email: Optional[str] = None
        self.user_password: Optional[str] = None
        self.password_validation: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.user_name = form.get("username")
        self.user_email = form.get("email")
        self.user_password = form.get("password")
        self.password_validation = form.get("password_validation")
        is_valid()


