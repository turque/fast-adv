from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_session
from api.models import User
from api.schemas import InviteSchema
from api.security import get_current_user

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/invite', tags=['teams'])


@router.post('/create', status_code=201)
def create_team(
    user: CurrentUser,
    invite: InviteSchema,
    session: Session = Depends(get_session),
):
    print(invite)
