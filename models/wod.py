from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from config.db import meta, engine

wods = Table("wods", meta,
              Column("wod_id", Integer, primary_key=True, autoincrement=True),
              Column("name", String(30)),
              Column("persons", Integer),
              Column("time_wod_h", Integer),
              Column("time_wod_m", Integer),
              Column("difficulty", Integer),
              Column("is_public", Boolean),
              Column("materials", String(199)),
              Column("description", String(300)),
              Column("creation_date", DateTime(timezone=True), server_default=func.now()),
              )

meta.create_all(engine)
