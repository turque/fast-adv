from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]

    teams: Mapped[list['Team']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )


class Team(Base):
    __tablename__ = 'teams'

    name: Mapped[str]
    team_members: Mapped[int]
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='teams')
