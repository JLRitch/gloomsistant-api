# standard modules
from typing import List, Optional

# external modules
from pydantic import BaseModel

# project modules

class Campaign(BaseModel):
    name: str
    gameMasterId: int
    missionsCompleted: List[int]
    missionsAvailable: List[int]
    eventsCompleted: List[int]
    itemsAvailable: List[int]
    characters: List[int]
    gameMasterFirstName: str
    gameMasterLastName: str
    gameMasterEmail: str