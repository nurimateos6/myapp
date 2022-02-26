from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.templating import Jinja2Templates
from models.user import users
from config.db import conn
from passlib.hash import pbkdf2_sha512
import os


templates = Jinja2Templates(directory='webapp/templates/')

SECRET = os.urandom(24).hex()
loginmanager = LoginManager(SECRET, token_url="/auth/login", use_cookie=True)
loginmanager.cookie_name = "foundmeqr"

log_in = APIRouter()


@loginmanager.user_loader()
def load_user(username: str):
    user = conn.execute(users.select().where(users.c.username == username)).first()
    return user


@log_in.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})


@log_in.post("/auth/login")
async def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    user = load_user(username)

    if not user:
        raise InvalidCredentialsException
    elif not pbkdf2_sha512.verify(data.password, user.password):
        return templates.TemplateResponse('login/login.html', {'request': request, 'errors': ["Incorrect username or password"]})
    access_token = loginmanager.create_access_token(
        data={"sub": username}
    )
    resp = RedirectResponse(url=f"/manager/account", status_code=status.HTTP_302_FOUND)
    loginmanager.set_cookie(resp, access_token)
    return resp
