from datetime import datetime
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.security import get_current_athlete
from app.core.settings import settings
from app.db.session import get_session
from app.models.invite import Invite
from app.utils.email import send_email

router = APIRouter()
Session = Annotated[Session, Depends(get_session)]
CurrentAthlete = Annotated[models.Athlete, Depends(get_current_athlete)]


@router.post('/create', response_model=schemas.Invite, status_code=201)
def create_invite(
    db: Session,
    current_athlete: CurrentAthlete,
    invite_in: schemas.InviteCreate,
) -> Any:

    # valida se time existe
    # valida se corrida existe

    team = db.scalar(
        select(Team).where(
            Team.id == invite.team_id, Team.owner_id == athlete.id
        )
    )

    if not team:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent team'
        )

    race = db.scalar(
        select(Race).where(
            Race.id == invite.race_id, Team.owner_id == athlete.id
        )
    )

    if not race:
        raise HTTPException(
            status_code=404, detail='Invalid or nonexistent race'
        )

    db_inviter = Invite(
        **invite.model_dump(mode='json'), token=str(token), athlete=athlete
    )

    db.add(db_inviter)
    db.commit()
    db.refresh(db_inviter)

    # TODO cadastrar convidado como atleta do time

    subject = f'Um convite especial de {athlete.name.capitalize}'

    sent = send_email(
        invite.email,
        invite.name,
        subject,
        settings.TEMPLATE_INVITE,
        receiver_name=invite.name,
        sender=athlete.name.capitalize,
        race=race.name,
        url_to_invite=settings.SERVER_HOST,
        token=db_inviter.token,
        team=team.name.capitalize,
    )
    if sent:
        db_inviter.sent_at = datetime.now()
        db.commit()
