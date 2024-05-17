from typing import Optional

from pydantic import BaseModel


class TeamBase(BaseModel):
    name: Optional[str]
    team_members: Optional[int]
    logo: Optional[str]
    # owner_id: Optional[int]
    race_id: Optional[int]


class TeamCreate(TeamBase):
    name: str


class TeamUpdate(TeamBase):
    pass


class TeamInDBBase(TeamBase):
    id: int
    name: str

    class Config:
        from_attributes = True


class Team(TeamInDBBase):
    pass


class TeamInDB(TeamInDBBase):
    pass
