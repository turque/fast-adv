from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

class AthleteScheme(BaseModel):
    

class AthleteSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class AthletePublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class AthleteDB(AthleteSchema):
    id: int


class AthleteList(BaseModel):
    athletes: list[AthletePublic]
