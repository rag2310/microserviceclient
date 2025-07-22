from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .configuration import Config

#prepare database connection
engine=create_engine(Config.SQLALCHEMY_DATABASE_URI)

#init orm session
local_session=sessionmaker(bind=engine)