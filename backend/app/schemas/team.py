from pydantic import BaseModel

# TODO migrate to CRUD format

class TeamSchema(BaseModel):
    name: str
    team_members: int
    race_id: int
    logo: str


class TeamPublic(BaseModel):
    id: int
    name: str
    team_members: int
    race_id: int


class TeamList(BaseModel):
    teams: list[TeamPublic]
