# standard modules
import pathlib as pl
import sqlite3

# external modules
from fastapi import FastAPI

# project modules
from db.connection import db_conn
from db import queryconverter


app = FastAPI()
cur = db_conn.cursor()

# TODO refactor routes to their own modules
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/players")
async def players():
    cur.execute(
        "SELECT * FROM player"
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "firstName", "lastName", "email"]
    )
    return resp_data