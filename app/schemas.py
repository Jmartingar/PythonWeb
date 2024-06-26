from pydantic import BaseModel #modelo con el cual se reciben los datos
from typing import Optional
from datetime import datetime

class Data(BaseModel):
    id: int
    date: datetime
    time: str
    site: str
    user_id: int

class Col(BaseModel):
    id: int
    min: float
    median: float
    max: float
    index: int

class Stat(BaseModel):
    id: int
    min_abs: float
    median_abs: float
    max_abs: float
    mean: Optional[float] = None
    mode: Optional[float] = None

class File(BaseModel):
    id: int
    name_cols: str

class Image(BaseModel):
    id: int
    name: str

class User(BaseModel): #Esquema que le llega al endpoint
    username: str
    password: str
    name: str
    surname: str
    email: str
    created_at: datetime = datetime.now()

class UserId(BaseModel):
    id: int