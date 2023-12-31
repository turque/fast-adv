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
