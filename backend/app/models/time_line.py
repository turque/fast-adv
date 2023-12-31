from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

if TYPE_CHECKING:
    from .race import Race  # noqa: F401


class TimeLine(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    stage: Mapped[str] = mapped_column(nullable=False)
    distance: Mapped[int] = mapped_column(nullable=True)
    estimated_time: Mapped[time] = mapped_column(nullable=True)
    observations: Mapped[str] = mapped_column(nullable=True)

    previous_stage: Mapped[int] = mapped_column(
        ForeignKey('timeline.id'), nullable=True
    )
    next_stage: Mapped[int] = mapped_column(
        ForeignKey('timeline.id'), nullable=True
    )

    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))
