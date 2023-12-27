from typing import TYPE_CHECKING

from datetime import time

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Time

from app.db.base_class import Base

from .enums import ModalityEnun

if TYPE_CHECKING:
    from .race import Race  # noqa: F401


class TimeLine(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    stage: Mapped[str] = mapped_column(nullable=False)
    distance: Mapped[int] = mapped_column(nullable=True)
    estimated_time: Mapped[time] = mapped_column(nullable=True)
    observations: Mapped[str] = mapped_column(nullable=True)

    previous_stage: Mapped[int] = mapped_column(ForeignKey('timeline.id'))
    next_stage: Mapped[int] = mapped_column(ForeignKey('timeline.id'))

    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))
