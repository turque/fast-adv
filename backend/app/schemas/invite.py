from pydantic import BaseModel, EmailStr


class InviteSchema(BaseModel):
    name: str
    email: EmailStr
    team: int
    race: int
