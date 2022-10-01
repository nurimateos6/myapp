from configparser import ConfigParser
from sqlalchemy import create_engine, MetaData

conf = ConfigParser()
conf.read('./config/conf.ini')

engine = create_engine(f"postgresql://{conf['db']['user']}:\
                        {conf['db']['password']}" \
                       f"@{conf['db']['host']}:\
                       {conf['db']['port']}/{conf['db']['schema']}")
meta = MetaData()
conn = engine.connect()
