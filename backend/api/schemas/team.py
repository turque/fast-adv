from pydantic import BaseModel


class TeamSchema(BaseModel):
    name: str
    team_members: int


class TeamPublic(BaseModel):
    id: int
    name: str
    team_members: int
    # owner_id: int


class TeamList(BaseModel):
    teams: list[TeamPublic]
