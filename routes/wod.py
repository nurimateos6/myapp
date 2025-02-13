from typing import List
from fastapi import Response, APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from config.db import conn
from models.wod import wods
from schemas.wod import Wod

principal = APIRouter()

templates = Jinja2Templates(directory="webapp/templates/")

key = Fernet.generate_key()
funcf = Fernet(key)

wod = APIRouter()


@wod.get('/wods/', response_model=List[Wod], tags=['Wods'])
def get_wod(request: Request):
    connection = get_wods()
    len_wods = len(connection)
    return templates.TemplateResponse('wods/wods.html', \
                                      {'request': request, \
                                       'wods': connection, \
                                       'len': len_wods})


@wod.get('/wods', response_model=List[Wod], tags=['Wods'])
def get_wods():
    return conn.execute(wods.select()).fetchall()


@wod.get('/{username}/wods/wods_form', response_model=Wod, tags=['Wods'])
def get_wod_form(request: Request):
    return templates.TemplateResponse('wods/wods_form.html', \
                                      {'request': request})


@wod.get('/{username}/wods/', response_model=List[Wod], tags=['Wods'])
def get_wod_user(username: str, request: Request):
    connection = get_wods()
    len_wods = len(connection)
    return templates.TemplateResponse('wods/wodsprivate.html',
                                      {'request': request, \
                                       'wods': connection, \
                                       'len': len_wods, \
                                       'username': username})


@wod.post('/wods', response_model=Wod, tags=['Wods'])
def add_wod(n_wod: Wod):
    new_wod = {'name': n_wod.name,
               'persons': n_wod.persons,
               'time_wod_h': n_wod.time_wod_h,
               'time_wod_m': n_wod.time_wod_m,
               'difficulty': n_wod.difficulty,
               'is_public': n_wod.is_public,
               "materials": n_wod.materials,
               'description': n_wod.description}

    res = conn.execute(wods.insert().values(new_wod))
    if res.is_insert:
        return conn.execute(wods.select().where(wods.c.wod_id == \
                                                res.inserted_primary_key[0])).first()  # pylint: disable=W0143
    return None


@wod.get("/wods/{wod_id}")
def get_wod_id():
    return conn.execute(wods.select().where(wods.c.wod_id == id)).first()  # pylint: disable=W0143


@wod.delete("/wods/{wod_id}")
def delete_wod():
    conn.execute(wods.delete().where(wods.c.wod_id == id)).first()  # pylint: disable=W0143
    return Response(status_code=HTTP_204_NO_CONTENT)


@wod.put('/wods/{wod_id}', response_model=Wod, tags=['Wods'])
def update_wod(n_wod: Wod):
    conn.execute(wods.update().values(
        wod_id=n_wod.wod_id,
        name=n_wod.name,
        persons=n_wod.persons
    ).where(wods.c.wod_id == id))  # pylint: disable=W0143
    return conn.execute(wods.select().where(wods.c.wod_id == id)).first()  # pylint: disable=W0143
