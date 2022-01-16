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

###########
# helper functions
###########
def fetch_campaign_id(camp_id: int) -> list:
    """
    Checks the database for a given campaign camp_id and raises and HTTPException 404 if not present.
    """
    cur.execute(
        "SELECT * FROM campaign WHERE campaign.id = ?",
        (camp_id,)
    )
    query = cur.fetchall()
    if query == []:
        raise HTTPException(status_code=404, detail=f"campaign with id {camp_id} not found.")
    return query

###########
# endpoints
###########
@router.get(
    "/campaigns",
    summary="Responds with summary data for all campaigns",
    description="Returns summary data for all campaigns"
)
async def get_campaigns():
    cur.execute(
        "SELECT id, name, characters FROM campaign"
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp=query,
        obj_keys=[
            "id", 
            "name", 
            "characters"
        ]
    )
    # reformat delimited lists into python lists (consider refactor to nosql db and bypass this need)
    for camp in resp_data:
        camp["characters"] = queryconverter.delimited_str_to_list(camp["characters"])
    
    return resp_data

@router.get(
    "/campaigns/{camp_id}",
    summary="Responds with a specific campaign's details",
    description="Returns all details associated with a given campaign"
)
async def get_campaigns(camp_id: int):
    query = fetch_campaign_id(camp_id=camp_id)
    resp_data = queryconverter.to_obj_array(
        query_resp=query,
        obj_keys=[
            "id", 
            "name", 
            "missionsCompleted", 
            "missionsAvailable", 
            "eventsCompleted", 
            "itemsAvailable",
            "characters"
        ]
    )
    # reformat delimited lists into python lists (consider refactor to nosql db and bypass this need)
    for camp in resp_data:
        camp["missionsCompleted"] = queryconverter.delimited_str_to_list(camp["missionsCompleted"])
        camp["missionsAvailable"] = queryconverter.delimited_str_to_list(camp["missionsAvailable"])
        camp["eventsCompleted"] = queryconverter.delimited_str_to_list(camp["eventsCompleted"])
        camp["itemsAvailable"] = queryconverter.delimited_str_to_list(camp["itemsAvailable"])
        camp["characters"] = queryconverter.delimited_str_to_list(camp["characters"])
    
    return resp_data

@router.post("campaigns")
async def create_campaign():
    pass