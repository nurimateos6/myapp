from sqlalchemy import create_engine, MetaData

PASSWORD = "your password"
engine = create_engine(f"postgresql://postgres:{PASSWORD}@0.0.0.0:5432/mymeals")

meta = MetaData()

conn = engine.connect()
