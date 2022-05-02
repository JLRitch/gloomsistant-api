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

def fetch_gamemaster_id(gm_id: int) -> list:
    """
    Checks the database for a given gamemaster gm_id and raises and HTTPException 404 if not present.
    """
    cur.execute(
        "SELECT * FROM player WHERE player.id = ?",
        (gm_id,)
    )
    query = cur.fetchall()
    if query == []:
        raise HTTPException(status_code=404, detail=f"player with id {gm_id} not found.")
    return query

def fetch_uniquecampaign_id(campaignName: str, gm_id: int) -> list:
    """
    Checks the database for a campaign with given gameMasterId and campaignName combo raises and 
    HTTPException 409 if it already exists.
    """
    cur.execute(
        "SELECT * FROM campaign WHERE gameMasterId = ? AND name = ?",
        (gm_id, campaignName)
    )
    query = cur.fetchall()
    if len(query) > 0:
        raise HTTPException(
            status_code=409,
            detail=f"campaign with gameMasterId {gm_id} and campaignName {campaignName} already exists.")
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
        "SELECT id, name, gameMasterId, characters FROM campaign"
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp=query,
        obj_keys=[
            "id", 
            "name",
            "gameMasterId",
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
async def get_campaign(camp_id: int):
    fetch_campaign_id(camp_id=camp_id)
    cur.execute(
        '''
            SELECT 
                campaign.*,
                player.firstName as gameMasterFirstName,
                player.lastName as gameMasterLastName,
                player.email as gameMasterEmail
            FROM campaign LEFT JOIN player on campaign.gameMasterId = player.id
            WHERE campaign.id = ?
        ''',
        (camp_id,)
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp=query,
        obj_keys=[
            "id", 
            "name",
            "gameMasterId",
            "missionsCompleted", 
            "missionsAvailable", 
            "eventsCompleted", 
            "itemsAvailable",
            "characters",
            "gameMasterFirstName",
            "gameMasterLastName",
            "gameMasterEmail"
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

@router.post("/campaigns")
async def create_campaign(
    campaignName: str,
    gameMasterId: int
):
    # check if the gameMasterId is a valid player
    fetch_gamemaster_id(gm_id=gameMasterId)
    # check if there is already a campaign with the given name and gm id
    fetch_uniquecampaign_id(campaignName=campaignName, gm_id=gameMasterId)
    # insert into db if checks pass
    cur.execute(
        "INSERT INTO campaign (name, gameMasterId, missionsAvailable) VALUES (?, ?, ?)",
        (campaignName, gameMasterId, 1)
    )
    db_conn.commit()
    return {"campaign successfully created!"}
    