from typing import Optional

from pydantic import BaseModel, EmailStr


class AthleteBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]


class AthleteCreate(AthleteBase):
    name: str
    password: Optional[str] = None


class AthleteUpdate(AthleteBase):
    password: Optional[str] = None


class AthleteInDBBase(AthleteBase):
    id: int

    class Config:
        from_attributes = True


class Athlete(AthleteInDBBase):
    pass


class AthleteInDB(AthleteInDBBase):
    pass
