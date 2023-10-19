from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]

    teams: Mapped[list['Team']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    team_members: Mapped[int]
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='teams')
