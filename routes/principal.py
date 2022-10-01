from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

principal = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")


@principal.get("/{username}/principal")
def get_home1(request: Request):
    return templates.TemplateResponse("principal.html", \
                                      {"request": request, "title": 'Home Page'})
