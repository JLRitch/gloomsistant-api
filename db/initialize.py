# standard modules
import pathlib as pl
import sqlite3

# project modules
from db.connection import db_conn

db_folder = pl.Path().cwd().joinpath("db")
cur = db_conn.cursor()

query_files = [f for f in db_folder.iterdir() if f.suffix == ".sql"]
for q in query_files:
    with open(q) as queryfile:
        cur.executescript(queryfile.read())