from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.settings import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)


def get_session():
    with Session(engine) as session:
        yield session
        session.close
