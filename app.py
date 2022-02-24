from routes.home import home
from routes.register import register
from routes.login import login
from routes.user import user
from fastapi import FastAPI
import os

app = FastAPI(
    title="My All in One",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }],
    version="0.0.1",

)


app.include_router(home)
app.include_router(user)
app.include_router(register)
app.include_router(login)


if __name__ == "__main__":
    os.system('uvicorn app:app --reload')
