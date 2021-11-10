# standard modules
from typing import Optional

# external modules
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

# project modules
from db.connection import db_conn
from db import queryconverter
from models.schemas.characters import Character


cur = db_conn.cursor()
router = APIRouter()

def fetch_character_id(id: int) -> list:
    """
    Checks the database for a given character id and raises and HTTPException 404 if not present.
    """
    cur.execute(
        "SELECT * FROM character WHERE character.id = ?",
        (id,)
    )
    query = cur.fetchall()
    if query == []:
        raise HTTPException(status_code=404, detail=f"character with id {id} not found.")
    return query

@router.get("/characters")
async def get_characters():
    cur.execute(
        "SELECT * FROM character"
    )
    query = cur.fetchall()
    query_array = queryconverter.to_obj_array(
        query_resp = query,
        obj_keys=["id", "name", "playerId", "characterClass", "level", "xp", "gold", "inventory", "goalsCompleted"]
    )
    resp_data = []
    for char in query_array:
        char["inventory"] = queryconverter.delimited_str_to_list(char["inventory"])
        resp_data.append(char)
    return resp_data

# @router.post("/characters")
# async def create_character(character: Character):
#     # check for duplicate email
#     cur.execute(
#         "SELECT * FROM character WHERE character.email = ?",
#         (character.email,)
#     )
#     query = cur.fetchall()
#     if len(query) > 0:
#         raise HTTPException(status_code=409, detail=f"character with email {character.email} already exists.")
#     # insert into db if new email address supplied
#     cur.execute(
#         "INSERT INTO character (firstName, lastName, email) VALUES (?, ?, ?)",
#         (character.firstName, character.lastName, character.email)
#     )
#     db_conn.commit()
#     return {"character successfully created!"}
