# standard modules
from typing import List, Optional

# external modules
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

# project modules
from db.connection import db_conn
from db import queryconverter
from models.schemas.characters import Character


cur = db_conn.cursor()
router = APIRouter()

def fetch_character_id(char_id: int) -> list:
    """
    Checks the database for a given character char_id and raises and HTTPException 404 if not present.
    """
    cur.execute(
        "SELECT * FROM character WHERE character.id = ?",
        (char_id,)
    )
    query = cur.fetchall()
    if query == []:
        raise HTTPException(status_code=404, detail=f"character with id {char_id} not found.")
    return query

@router.get("/characters")
async def get_characters(char_ids):
    try:
        q_list = ("?,"*len(char_ids))[:-1]
    except IndexError: # assumed char_ids is empty
        q_list = None
    query = f"SELECT * FROM character WHERE character.id IN ({q_list})"
    cur.execute(
        query,
        char_ids
    )
    query = cur.fetchall()
    query_array = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "name", "playerId", "characterClass", "level", "xp", "gold", "inventory", "goalsCompleted"]
    )
    if query == []:
        raise HTTPException(status_code=404, detail=f"character with id {char_ids} not found.")
    resp_data = []
    for char in query_array:
        char["inventory"] = queryconverter.delimited_str_to_list(char["inventory"])
        resp_data.append(char)
    return resp_data

@router.post("/characters")
async def create_character(
    characterName: str,
    characterClass: str,
    playerId: int
):
    # check for an existing character of this class for the given name & playerid
    query = "SELECT * FROM character WHERE character.name = ? AND character.playerid = ? AND character.characterClass = ?"
    cur.execute(
        query,
        (characterName, playerId, characterClass)
    )
    query = cur.fetchall()
    if len(query) > 0:
        raise HTTPException(
            status_code=409,
            detail=f"The playerid {playerId} already has a {characterClass} named {characterName}."
        )
    # insert into db if it appears to be a new character
    cur.execute(
        "INSERT INTO character (name, characterClass, playerId, level, xp, gold, goalsCompleted) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (characterName, characterClass, playerId, 1, 0, 0, 0),
    )
    db_conn.commit()
    return {"character successfully created!"}
