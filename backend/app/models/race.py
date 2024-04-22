from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .athlete import Athlete  # noqa: F401


class Race(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(nullable=False)
    place: Mapped[str] = mapped_column(nullable=True)
    race_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    distance: Mapped[int] = mapped_column(nullable=True)
    url_race: Mapped[str] = mapped_column(nullable=True)
    race_description: Mapped[str] = mapped_column(nullable=True)
    place_description: Mapped[str] = mapped_column(nullable=True)
    observations: Mapped[str] = mapped_column(nullable=True)
    athlete_id: Mapped[int] = mapped_column(ForeignKey('athlete.id'))

    athlete: Mapped['Athlete'] = relationship(back_populates='races')
