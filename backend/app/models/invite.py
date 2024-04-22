from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .athlete import Athlete  # noqa: F401


class Invite(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    token: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    team_id: Mapped[int] = mapped_column(nullable=False)
    race_id: Mapped[int] = mapped_column(nullable=False)
    athlete_id: Mapped[int] = mapped_column(ForeignKey('athlete.id'))
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    athlete: Mapped['Athlete'] = relationship(back_populates='invites')
