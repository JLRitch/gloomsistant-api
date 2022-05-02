# standard modules
from typing import List, Optional

# external modules
from pydantic import BaseModel

# project modules
# from models.schemas.gloom import RWSchema


class Player(BaseModel):
    id: int=None
    firstName: str
    lastName: str
    email: str