# standard modules
from typing import List, Optional

# external modules
from pydantic import BaseModel

# project modules

class Campaign(BaseModel):
    name: str
    missionsCompleted: List[str]
    missionsAvailable: List[str]
    eventsCompleted: List[str]
    itemsAvailable: List[str]