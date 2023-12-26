from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

if TYPE_CHECKING:
    from .race import Race  # noqa: F401
    from .user import User  # noqa: F401


class TeamRace(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))
