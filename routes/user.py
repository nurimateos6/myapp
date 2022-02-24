from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

key = Fernet.generate_key()
key = Fernet(key)

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post('/users', response_model=User, tags=['Users'])
def create_user(user: User):
    new_user = {'username': user.username,
                'email': user.email,
                'password': key.encrypt(user.password.encode('utf-8'))}

    res = conn.execute(users.insert().values(new_user))
    if res.is_insert:
        return conn.execute(users.select().where(users.c.id == res.inserted_primary_key[0])).first()
    else:
        return {}

@user.get("/users/{id}")
def get_user():
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}")
def delete_user():
    conn.execute(users.delete().where(users.c.id == id)).first()
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put('/users/{id}', response_model=User, tags=['Users'])
def update_user(id: int, user: User):
    conn.execute(users.update().values(
        username=user.username,
        password=key.encrypt(user.password.encode('utf-8')),
        email=user.email
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()