from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


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


class Team(Base):
    __tablename__ = 'teams'

    name: Mapped[str] = mapped_column(nullable=False, index=True)
    team_members: Mapped[int]
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='teams')


class Invite(Base):
    __tablename__ = 'invites'

    invite: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    guest_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='invites')
