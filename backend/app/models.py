from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(nullable=True, default=True)

    teams: Mapped[list['Team']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )
    invites: Mapped[list['Invite']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )
    races: Mapped[list['Race']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )


class Team(Base):
    __tablename__ = 'teams'

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    team_members: Mapped[int]
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='teams')


class Invite(Base):
    __tablename__ = 'invites'

    token: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    team: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    user: Mapped[User] = relationship(back_populates='invites')


class Race(Base):
    __tablename__ = 'races'

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
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='races')
