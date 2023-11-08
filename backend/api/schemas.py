from pydantic import BaseModel, ConfigDict, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Message(BaseModel):
    detail: str


class TeamSchema(BaseModel):
    name: str
    team_members: int


class TeamPublic(BaseModel):
    id: int
    name: str
    team_members: int


class TeamList(BaseModel):
    teams: list[TeamPublic]


class InviteSchema(BaseModel):
    name: str
    email: EmailStr
    team: int


class RaceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class RacePublic(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class RaceList(BaseModel):
    races: list[RacePublic]
