from typing import Optional

from fastapi import APIRouter, Body, Depends
from starlette import status

# project modules
from db.connection import db_conn
from db import queryconverter


cur = db_conn.cursor()
router = APIRouter()


@router.get("")
async def get_players():
    cur.execute(
        "SELECT * FROM player"
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "firstName", "lastName", "email"]
    )
    return resp_data