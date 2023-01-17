#-------------------------------------------------------------------------------
# Snippet to use python-oracledb in SQLAlchemy 1.4
# (not needed in SQLAlchemy 2)

import oracledb
import sys
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

# end snippet

#-------------------------------------------------------------------------------
import os
from sqlalchemy import create_engine

MAGIC_USER = os.getenv("MAGIC_USER")
MAGIC_PASSWORD = os.getenv("MAGIC_PASSWORD")
CURRENT_SCHEMA = "MAGIC_POOL"
DATABASE_SERVICE_NAME = 'defr6-bcsexa-i01-g3-scan/fra18r_MAGICP.bayer.cnb'
hostname, service_name = DATABASE_SERVICE_NAME.split("/")
port = 1521

def create_magic_engine():
    return create_engine(f'oracle://{MAGIC_USER}:{MAGIC_PASSWORD}@{hostname}:{port}/?service_name={service_name}')
