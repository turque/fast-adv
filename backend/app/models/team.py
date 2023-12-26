from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Team(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    team_members: Mapped[int] = mapped_column(nullable=False)
    logo: Mapped[str] = mapped_column(nullable=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    race_id: Mapped[int] = mapped_column(ForeignKey('race.id'))
    user: Mapped['User'] = relationship(back_populates='teams')
