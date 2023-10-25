import uuid

# from datetime import datetime
# from hashlib import sha256
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.database import get_session
from api.models import Invite, Team, User
from api.schemas import InviteSchema
from api.security import get_current_user

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/invite', tags=['invites'])


@router.post('/create', status_code=201)
def create_team(
    user: CurrentUser,
    invite: InviteSchema,
    session: Session = Depends(get_session),
):
    team = session.scalar(
        select(Team).where(Team.id == invite.team, Team.owner_id == user.id)
    )

    if not team:
        raise HTTPException(status_code=404, detail='Invalid or absent team')

    token = uuid.uuid4()

    db_inviter = Invite(**invite.dict(), token=str(token), user_id=user.id)

    session.add(db_inviter)
    session.commit()
    session.refresh(db_inviter)


    # TODO cadastrar convidado como atleta do time
    # TODO codificar o nome e e-mail com base64 e gerar o hash
    # TODO disparar o convite via e-mail
