from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql import func
from config.db import meta, engine

recipes = Table("recipes", meta,
              Column("recipe_id", Integer, primary_key=True, autoincrement=True),
              Column("name", String(30)),
              Column("servings", Integer),
              Column("time_preparation_h", Integer),
              Column("time_preparation_m", Integer),
              Column("difficulty", Integer),
              Column("is_public", String(100)),
              Column("ingredients", String(199)),
              Column("description", String(300)),
              Column("creation_date", DateTime(timezone=True), server_default=func.now()),
              )

meta.create_all(engine)
