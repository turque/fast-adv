from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

if TYPE_CHECKING:
    from .race import Race  # noqa: F401
    from .user import User  # noqa: F401


class StrategicPlanning(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    mission: Mapped[str] = mapped_column(nullable=True)
    vision: Mapped[str] = mapped_column(nullable=True)
    values: Mapped[str] = mapped_column(nullable=True)
    strategic_objectives: Mapped[str] = mapped_column(nullable=True)
    immediate_objectives: Mapped[str] = mapped_column(nullable=True)
    strengths: Mapped[str] = mapped_column(nullable=True)
    weaknesses: Mapped[str] = mapped_column(nullable=True)
    opportunities: Mapped[str] = mapped_column(nullable=True)
    threats: Mapped[str] = mapped_column(nullable=True)

    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
