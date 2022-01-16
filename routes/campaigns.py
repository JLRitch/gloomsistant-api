# standard modules
from typing import List, Optional

# external modules
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

# project modules
from db.connection import db_conn
from db import queryconverter


cur = db_conn.cursor()
router = APIRouter()

@router.get("/campaigns")
async def get_campaigns():
    cur.execute(
        "SELECT * FROM campaign"
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp=query,
        obj_keys=[
            "id", 
            "name", 
            "missionsCompleted", 
            "missionsAvailable", 
            "eventsCompleted", 
            "itemsAvailable"
        ]
    )
    # reformat delimited lists into python lists (consider refactor to nosql db and bypass this need)
    for camp in resp_data:
        camp["missionsCompleted"] = queryconverter.delimited_str_to_list(camp["missionsCompleted"])
        camp["missionsAvailable"] = queryconverter.delimited_str_to_list(camp["missionsAvailable"])
        camp["eventsCompleted"] = queryconverter.delimited_str_to_list(camp["eventsCompleted"])
        camp["itemsAvailable"] = queryconverter.delimited_str_to_list(camp["itemsAvailable"])
    
    return resp_data