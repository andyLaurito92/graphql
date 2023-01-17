#-------------------------------------------------------------------------------
# Snippet to use python-oracledb in SQLAlchemy 1.4
# (not needed in SQLAlchemy 2)

import oracledb
import sys
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

# end snippet

#-------------------------------------------------------------------------------
from graphene import ObjectType, NonNull, String, List, Schema
from magic_connection import create_magic_engine
import pandas as pd

magic_pool_engine = create_magic_engine()

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `first_name`
    # By default, the argument name will automatically be camel-based into firstName in the generated schema
    all_countries = List(String)

    def resolve_all_countries(root, info):
        return [tup[1] for tup in magic_pool_engine.execute("SELECT * FROM MAGIC_POOL.CUCNOB_COUNTRY_CNT").fetchall()]

schema = Schema(query=Query)
