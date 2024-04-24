from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .invite import Invite  # noqa: F401
    from .race import Race  # noqa: F401
    from .team import Team  # noqa: F401


class Athlete(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(nullable=True, default=True)
    invites: Mapped[list['Invite']] = relationship(
        back_populates='athlete', cascade='all, delete-orphan'
    )
    races: Mapped[list['Race']] = relationship(
        back_populates='athlete', cascade='all, delete-orphan'
    )
    teams: Mapped[list['Team']] = relationship(
        back_populates='athlete', cascade='all, delete-orphan'
    )
