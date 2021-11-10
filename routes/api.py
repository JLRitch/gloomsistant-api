# standard modules
import pathlib as pl
import sqlite3

# external modules
from fastapi import APIRouter

# project modules
from routes import players, characters


router = APIRouter()
router.include_router(players.router, tags=["players"])
router.include_router(characters.router, tags=["characters"])
