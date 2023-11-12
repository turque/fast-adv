from pydantic import BaseModel, ConfigDict


class RaceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class RacePublic(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class RaceList(BaseModel):
    races: list[RacePublic]
