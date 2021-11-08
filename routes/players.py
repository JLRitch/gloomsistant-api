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
    "/players/{id}",
    summary="Responds with a specific player's details",
    description="Returns all the details associated with a given player"
)
async def get_players(id: int):
    cur.execute(
        "SELECT * FROM player WHERE player.id = ?",
        (id,)
    )
    query = cur.fetchall()
    resp_data = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "firstName", "lastName", "email"]
    )
    if resp_data == []:
        raise HTTPException(status_code=404, detail=f"Player with id {id} not found.")
    return resp_data