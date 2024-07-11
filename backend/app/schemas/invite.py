from typing import Optional

from pydantic import BaseModel, EmailStr


class InviteBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    team_id: Optional[int]
    race_id: Optional[int]


class InviteCreate(InviteBase):
    name: str
    email: EmailStr


class InviteUpdate(InviteBase):
    pass


class InviteInDBBase(InviteBase):
    id: int

    class Config:
        from_attributes = True


class Invite(InviteInDBBase):
    pass


class InviteInDB(InviteInDBBase):
    pass
