# standard modules
from typing import Optional

# external modules
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

# project modules
from db.connection import db_conn
from db import queryconverter
from models.schemas.players import Player


cur = db_conn.cursor()
router = APIRouter()

###########
# helper functions
###########
def fetch_player_id(player_id: int) -> list:
    """
    Checks the database for a given player id and raises and HTTPException 404 if not present.
    """
    cur.execute(
        "SELECT * FROM player WHERE player.id = ?",
        (player_id,)
    )
    query = cur.fetchall()
    if query == []:
        raise HTTPException(status_code=404, detail=f"Player with id {player_id} not found.")
    return query

###########
# endpoints
###########
@router.get("/players")
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

@router.post("/players")
async def create_player(player: Player):
    # check for duplicate email
    cur.execute(
        "SELECT * FROM player WHERE player.email = ?",
        (player.email,)
    )
    query = cur.fetchall()
    if len(query) > 0:
        raise HTTPException(status_code=409, detail=f"Player with email {player.email} already exists.")
    # insert into db if new email address supplied
    cur.execute(
        "INSERT INTO player (firstName, lastName, email) VALUES (?, ?, ?)",
        (player.firstName, player.lastName, player.email)
    )
    db_conn.commit()
    return {"player successfully created!"}

@router.get(
    "/players/{player_id}",
    summary="Responds with a specific player's details",
    description="Returns all the details associated with a given player"
)
async def get_player_id(player_id: int):
    query = fetch_player_id(player_id)
    resp_data = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "firstName", "lastName", "email"]
    )
    return resp_data

@router.put(
    "/players/{player_id}",
    summary="Updates a specific player's details",
    description="Updates the details associated with a given player"
)
async def update_player(player_id: int, player: Player):
    # check if player exists, raise error if not
    fetch_player_id(player_id)
    # update player if it exists
    cur.execute(
        """
            UPDATE player 
            SET firstName = ?,
                lastName = ?,
                email = ?
            WHERE
                player.id = ?;
        """,
        (
            player.firstName,
            player.lastName,
            player.email,
            player_id
        )
    )
    db_conn.commit()
    return {f"player {player_id} successfully updated!"}

@router.delete(
    "/players/{player_id}",
    summary="Deletes a specific player",
    description="Delete a player given a specific id"
)
async def delete_player(player_id: int):
    fetch_player_id(player_id)
    cur.execute(
        "DELETE FROM player WHERE player.id = ?",
        (player_id, )
    )
    db_conn.commit()
    return {f"player {player_id} successfully deleted, hope you meant to do that!"}