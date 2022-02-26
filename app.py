from routes.home import home
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from routes.register import registration
from routes.login import log_in
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

app.mount(
    "/static",
    StaticFiles(directory=Path("/Users/nurimateos/Desktop/quer_me 2/webapp/static")),
    #StaticFiles(directory=Path(__file__).parent.parent.absolute() / "webapp/static"),
    name="static",
)

app.include_router(home)
app.include_router(user)
app.include_router(registration)
app.include_router(log_in)


if __name__ == "__main__":
    os.system('uvicorn app:app --reload')
