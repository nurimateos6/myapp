from fastapi import APIRouter, Response
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

key = Fernet.generate_key()
key = Fernet(key)


@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post('/users', response_model=User, tags=['Users'])
def create_user(n_user: User):
    new_user = {'username': n_user.username,
                'email': n_user.email,
                'password': key.encrypt(n_user.password.encode('utf-8'))}

    res = conn.execute(users.insert().values(new_user))
    if res.is_insert:
        return conn.execute(
            users.select().where(users.c.id == res.inserted_primary_key[0])).first()  # pylint: disable=W0143
    return None


@user.get("/users/{id}")
def get_user():
    return conn.execute(users.select().where(users.c.id == id)).first()  # pylint: disable=W0143


@user.delete("/users/{id}")
def delete_user():
    conn.execute(users.delete().where(users.c.id == id)).first()  # pylint: disable=W0143
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put('/users/{id}', response_model=User, tags=['Users'])
def update_user(user_id: int, n_user: User):
    conn.execute(users.update().values(
        username=n_user.username,
        password=key.encrypt(n_user.password.encode('utf-8')),
        email=n_user.email
    ).where(users.c.id == user_id))
    return conn.execute(users.select().where(users.c.id == user_id)).first()  # pylint: disable=W0143
