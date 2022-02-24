from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

login = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")


@login.get("/login/")
def get_home(request: Request):
    return templates.TemplateResponse("/login/login.html", {"request": request})

