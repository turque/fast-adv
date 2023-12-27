from pydantic import BaseModel, EmailStr


class InviteSchema(BaseModel):
    name: str
    email: EmailStr
    team_id: int
    race_id: int
