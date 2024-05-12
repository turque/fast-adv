from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

if TYPE_CHECKING:
    from .race import Race  # noqa: F401


class Fugleman(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    email: Mapped[str] = mapped_column(nullable=True, index=True)
    phone: Mapped[str] = mapped_column(nullable=True)

    race_id: Mapped['Race'] = mapped_column(ForeignKey('race.id'))
