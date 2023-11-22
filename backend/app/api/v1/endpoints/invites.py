import uuid
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.core.settings import settings
from app.db.session import get_session
from app.models import Invite, Race, Team, User
from app.schemas import InviteSchema
from app.utils.email import send_email

CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter()


@router.post('/create', status_code=201)
def create_invite(
    user: CurrentUser,
    invite: InviteSchema,
    db: Session = Depends(get_session),
):
    team = db.scalar(
        select(Team).where(Team.id == invite.team, Team.owner_id == user.id)
    )

    if not team:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent team'
        )

    race = db.scalar(
        select(Race).where(Race.id == invite.race, Team.owner_id == user.id)
    )

    if not race:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent race'
        )

    token = uuid.uuid4()

    db_inviter = Invite(
        **invite.model_dump(mode='json'), token=str(token), user_id=user.id
    )

    db.add(db_inviter)
    db.commit()
    db.refresh(db_inviter)

    # TODO cadastrar convidado como atleta do time

    subject = f'Um convite especial de {user.name.capitalize}'

    sent = send_email(
        invite.email,
        invite.name,
        subject,
        settings.TEMPLATE_INVITE,
        receiver_name=invite.name,
        sender=user.name.capitalize,
        race=race.name,
        url_to_invite=settings.SERVER_HOST,
        token=db_inviter.token,
        team=team.name.capitalize,
    )
    if sent:
        db_inviter.sent_at = datetime.now()
        db.commit()
