import uuid
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Invite, invite
from app.schemas.invite import InviteCreate, InviteUpdate


class CRUDInvite(CRUDBase[Invite, InviteCreate, InviteUpdate]):
    def create(
        self, db: Session, *, invite_in: InviteCreate, athlete_id: int
    ) -> Invite:
        db_invite = Invite(**invite_in.model_dump(), athlete_id=athlete_id)
        db_invite.token = uuid.uuid4()
        db.add(db_invite)
        db.commit()
        db.refresh(db_invite)
        return db_invite

    def get_by_id(self, db: Session, *, invite_id) -> Invite:
        return db.scalars(select(Invite).where(Invite.id == invite_id))

    def get_by_token(self, db: Session, *, token) -> Invite:
        return db.scalars(select(Invite).where(Invite.token == token))


invite = CRUDInvite(Invite)
