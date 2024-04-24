import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import get_password_hash
from app.db.base import Base
from app.db.session import get_session
from app.main import app

from .factory import (
    AthleteFactory,
    EquipamentsFactory,
    RaceFactory,
    StrategicPlanningFactory,
    TeamFactory,
)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def athlete(session):
    password = 'testtest'
    athlete = AthleteFactory(password=get_password_hash(password))

    session.add(athlete)
    session.commit()
    session.refresh(athlete)

    athlete.clean_password = 'testtest'

    yield athlete


@pytest.fixture
def other_athlete(session):
    password = 'testtest'
    athlete = AthleteFactory(password=get_password_hash(password))

    session.add(athlete)
    session.commit()
    session.refresh(athlete)

    athlete.clean_password = 'testtest'

    yield athlete


@pytest.fixture
def token(client, athlete):
    response = client.post(
        'api/v1/auth/token',
        data={'username': athlete.email, 'password': athlete.clean_password},
    )
    return response.json()['access_token']


@pytest.fixture
def team(session, athlete, race):
    team = TeamFactory(
        owner_id=athlete.id,
        race_id=race.id,
    )

    session.add(team)

    session.commit()
    session.refresh(team)

    yield team


@pytest.fixture
def other_team(session, other_athlete):
    owner_id = other_athlete.id
    team = TeamFactory(owner_id=owner_id)

    session.add(team)

    session.commit()
    session.refresh(team)

    yield team


@pytest.fixture
def race(session, athlete):
    athlete_id = athlete.id
    race = RaceFactory(athlete_id=athlete_id)

    session.add(race)

    session.commit()
    session.refresh(race)

    yield race


@pytest.fixture
def strategic_planning(session, athlete, race):
    athlete_id = athlete.id
    race_id = race.id
    strategic = StrategicPlanningFactory(
        athlete_id=athlete_id, race_id=race_id
    )

    session.add(strategic)

    session.commit()
    session.refresh(strategic)

    yield strategic


@pytest.fixture
def equipament(session, race):
    race_id = race.id
    equipament = EquipamentsFactory(race_id=race_id)

    session.add(equipament)

    session.commit()
    session.refresh(equipament)

    yield equipament
