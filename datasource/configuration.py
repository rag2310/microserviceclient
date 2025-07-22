import os
from .secrets import getSecret

name_db=os.getenv("NAME_DB")
user_db=getSecret("db-user")
password_db=getSecret("db-password")
ip_db=os.getenv("IP_DB")
port_db=os.getenv("PORT_DB")

class Config:
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{user_db}:{password_db}@{ip_db}:{port_db}/{name_db}"
    SQL_ALCHEMY_TRACK_MODIFICATIONS=False