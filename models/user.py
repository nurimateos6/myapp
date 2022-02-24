from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql import func
from config.db import meta, engine

users = Table("users", meta,
              Column("id", Integer, primary_key=True, autoincrement=True),
              Column("username", String(30)),
              Column("password", String(22)),
              Column("email", String(50)),
              Column("modification_date", DateTime(timezone=True), onupdate=func.now()),
              Column("creation_date", DateTime(timezone=True), server_default=func.now())
              )

meta.create_all(engine)
