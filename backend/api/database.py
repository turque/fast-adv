from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from api.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


class Base(DeclarativeBase):
    """Base database model."""

    id: Mapped[int] = mapped_column(primary_key=True)
