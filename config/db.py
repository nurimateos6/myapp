from sqlalchemy import create_engine, MetaData
from configparser import ConfigParser

conf = ConfigParser()
conf.read('./config/conf.ini')

engine = create_engine(f"postgresql://{conf['db']['user']}:{conf['db']['password']}@{conf['db']['host']}:{conf['db']['port']}/{conf['db']['schema']}")
meta = MetaData()

conn = engine.connect()


