from datetime import date
from typing import Optional

from pydantic import BaseModel


class RaceBase(BaseModel):
    name: Optional[str]
    place: Optional[str]
    race_date: Optional[date]
    distance: Optional[int]
    url_race: Optional[str]
    race_description: Optional[str]
    place_description: Optional[str]
    observations: Optional[str]


class RaceCreate(RaceBase):
    name: str


class RaceUpdate(RaceBase):
    pass


class RaceInDBBase(RaceBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Race(RaceInDBBase):
    pass


class RaceInDB(RaceInDBBase):
    pass
