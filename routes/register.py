from typing import List
from fastapi import APIRouter, Request, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha512
from webapp.forms.registrations import RegistrationForm
from schemas.user import User
from models.user import users
from config.db import conn


registration = APIRouter()

templates = Jinja2Templates(directory='webapp/templates/')


@registration.get('/registration/', response_model=List[User], tags=['Registration'])
def get_registration(request: Request):
    return templates.TemplateResponse('register/register.html', {'request': request})


@registration.post('/registration/')
async def create_registration(request: Request):
    form = RegistrationForm(request)
    await form.load_data()
    if await form.is_valid():
        new_user = {'username': form.username,
                    'email': form.email,
                    'password': pbkdf2_sha512.using(rounds=1000, salt_size=13).hash(form.password)}
        try:
            res = conn.execute(users.insert().values(new_user))
            if res.is_insert:
                return responses.RedirectResponse(
                    '/login/', status_code=status.HTTP_302_FOUND
                )
        except IntegrityError:
            form.__dict__.get('errors').append('Duplicate username or email')
    return templates.TemplateResponse('register/register.html', form.__dict__)
