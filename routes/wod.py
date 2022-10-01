from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.wod import wods
from models.user import users
from schemas.wod import Wod
from typing import List
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

principal = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")

from cryptography.fernet import Fernet

key = Fernet.generate_key()
funcf = Fernet(key)

wod = APIRouter()

@wod.get('/wods/', response_model=List[Wod], tags=['Wods'])
def get_wod(request: Request):
    conn = get_wods()
    len_wods = len(conn)
    return templates.TemplateResponse('wods/wods.html', {'request': request, 'wods': conn, 'len': len_wods})

@wod.get('/wods', response_model=List[Wod], tags=['Wods'])
def get_wods():
    return conn.execute(wods.select()).fetchall()

@wod.get('/{username}/wods/wods_form', response_model=Wod, tags=['Wods'])
def get_wod_form(request: Request):
    return templates.TemplateResponse('wods/wods_form.html', {'request': request})

@wod.get('/{username}/wods/', response_model=List[Wod], tags=['Wods'])
def get_wod_user(username: str, request: Request):
    conn = get_wods()
    len_wods = len(conn)
    return templates.TemplateResponse('wods/wodsprivate.html', {'request': request, 'wods':conn, 'len': len_wods, 'username': username})


@wod.post('/wods', response_model=Wod, tags=['Wods'])
def add_wod(wod: Wod):
    new_wod = {'name': wod.name,
                  'persons': wod.persons,
                  'time_wod_h': wod.time_wod_h,
                  'time_wod_m': wod.time_wod_m,
                  'difficulty': wod.difficulty,
                  'is_public': wod.is_public,
                  "materials": wod.materials,
                  'description': wod.description}

    res = conn.execute(wods.insert().values(new_wod))
    if res.is_insert:
        return conn.execute(wods.select().where(wods.c.wod_id == res.inserted_primary_key[0])).first()
    else:
        return {}


@wod.get("/wods/{wod_id}")
def get_wod():
    return conn.execute(wods.select().where(wods.c.wod_id == id)).first()


@wod.delete("/wods/{wod_id}")
def delete_wod():
    conn.execute(wods.delete().where(wods.c.wod_id == id)).first()
    return Response(status_code=HTTP_204_NO_CONTENT)


@wod.put('/wods/{wod_id}', response_model=Wod, tags=['Wods'])
def update_wod(wod_id: int, wod: Wod):
    conn.execute(wods.update().values(
        wod_id=wod.wod_id,
        name=wod.name,
        persons=wod.persons
    ).where(wods.c.wod_id == id))
    return conn.execute(wods.select().where(wods.c.wod_id == id)).first()