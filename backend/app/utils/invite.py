from datetime import datetime

from sqlalchemy.orm import Session

from app import crud
from app.core.settings import settings
from app.schemas.invite import Invite, InviteUpdate
from app.services.email import send_email


def send_invite(
    db: Session,
    *,
    invite: Invite,
    sender: str,
    race_name: str,
    team_name: str,
):
    invite_in = InviteUpdate
    subject = f'Um convite especial de {sender.capitalize}'

    sent = send_email(
        invite.email,
        invite.name,
        subject,
        settings.TEMPLATE_INVITE,
        receiver_name=invite.name,
        sender=sender.capitalize,
        race=race_name,
        url_to_invite=settings.SERVER_HOST,
        token=invite.token,
        team=team_name.capitalize,
    )
    if sent:
        invite.send_at = datetime.now()
        crud.invite.update(db=db, db_obj=invite, obj_in=invite_in)
