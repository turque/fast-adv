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
    EquipamentsFactory,
    RaceFactory,
    StrategicPlanningFactory,
    TeamFactory,
    UserFactory,
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
def user(session):
    password = 'testtest'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'

    yield user


@pytest.fixture
def other_user(session):
    password = 'testtest'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'

    yield user


@pytest.fixture
def token(client, user):
    response = client.post(
        'api/v1/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']


@pytest.fixture
def team(session, user, race):
    team = TeamFactory(
        owner_id=user.id,
        race_id=race.id,
    )

    session.add(team)

    session.commit()
    session.refresh(team)

    yield team


@pytest.fixture
def other_team(session, other_user):
    owner_id = other_user.id
    team = TeamFactory(owner_id=owner_id)

    session.add(team)

    session.commit()
    session.refresh(team)

    yield team


@pytest.fixture
def race(session, user):
    user_id = user.id
    race = RaceFactory(user_id=user_id)

    session.add(race)

    session.commit()
    session.refresh(race)

    yield race


@pytest.fixture
def strategic_planning(session, user, race):
    user_id = user.id
    race_id = race.id
    strategic = StrategicPlanningFactory(user_id=user_id, race_id=race_id)

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
