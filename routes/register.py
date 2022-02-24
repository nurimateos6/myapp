from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

register = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")


@register.get("/registration/")
def get_home(request: Request):
    return templates.TemplateResponse("/register/register.html", {"request": request})
