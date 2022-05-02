# standard modules
import pathlib as pl
import sqlite3

# project modules
from db.connection import db_conn

db_folder = pl.Path().cwd().joinpath("db")
cur = db_conn.cursor()

create_files = [f for f in db_folder.iterdir() if f.suffix == ".sql" and "create" in f.name]
for q in create_files:
    print(f"Running {q}...")
    with open(q) as queryfile:
        cur.executescript(queryfile.read())
    db_conn.commit()

example_files = [f for f in db_folder.iterdir() if f.suffix == ".sql" and "example" in f.name]
for q in example_files:
    print(f"Running {q}...")
    with open(q) as queryfile:
        cur.executescript(queryfile.read())
    db_conn.commit()