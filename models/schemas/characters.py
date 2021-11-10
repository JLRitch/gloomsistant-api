# standard modules
from typing import List, Optional

# external modules
from pydantic import BaseModel

# project modules

class Perk(BaseModel):
    perkDesc: str
    perkLevel: int

class Character(BaseModel):
    name: str
    playerId: int
    characterClass: str
    level: int=1
    xp: int=0
    gold: int=0
    inventory: List[str]=[]
    perks: List[Perk]=[]
    goalsCompleted: int=0
