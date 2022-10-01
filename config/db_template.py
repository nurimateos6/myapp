from sqlalchemy import create_engine, MetaData

password = "your password"
engine = create_engine(f"postgresql://postgres:{password}@0.0.0.0:5432/mymeals")

meta = MetaData()

conn = engine.connect()
