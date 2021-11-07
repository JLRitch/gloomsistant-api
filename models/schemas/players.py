# standard modules
from typing import List, Optional

# external modules
from pydantic import BaseModel

# project modules
# from models.schemas.gloom import RWSchema


class Player(BaseModel):
    firstName: str
    lastName: str
    email: str


# class CommentInResponse(RWSchema):
#     comment: Comment


# class CommentInCreate(RWSchema):
#     body: str