from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

if TYPE_CHECKING:
    from .equipaments import Equipaments  # noqa: F401
    from .user import User  # noqa: F401


class EquipamentsAthlete(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    observations: Mapped[str] = mapped_column(nullable=False)
    have: Mapped[bool] = mapped_column(nullable=True, default=True)
    ready: Mapped[bool] = mapped_column(nullable=True, default=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    equipament_id: Mapped[int] = mapped_column(ForeignKey('equipaments.id'))
