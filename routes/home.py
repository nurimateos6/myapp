from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

home = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")


@home.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": 'Home Page'})
