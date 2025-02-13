import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.home import home
from routes.register import registration
from routes.login import log_in
from routes.user import user
from routes.principal import principal


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
    StaticFiles(directory=Path("/Users/nurimateos/PycharmProjects/myapp/webapp/static")),
    #StaticFiles(directory=Path(__file__).parent.parent.absolute() / "webapp/static"),
    name="static",
)

app.include_router(home)
app.include_router(user)
app.include_router(registration)
app.include_router(log_in)
app.include_router(principal)


if __name__ == "__main__":
    os.system('uvicorn app:app --reload')
