# standard modules
import pathlib as pl
import sqlite3

# external modules
from fastapi import APIRouter

# project modules
from routes import players


router = APIRouter()
router.include_router(players.router, tags=["players"], prefix="/players")
