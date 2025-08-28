from pydantic import BaseModel
import os
from typing import Optional
from datetime import datetime


class UsersOut(BaseModel):
    id: int
    nombre: str
    fec_add: datetime

class UserOut(BaseModel):
    nombre: str

class ForumUser(BaseModel):
    nombre: str  