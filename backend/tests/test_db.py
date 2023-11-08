from datetime import datetime

from sqlalchemy import select

from api.models import Invite, Race, Team, User


def test_create_user(session):
    new_user = User(name='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.name == 'alice'))

    assert user.name == 'alice'


def test_create_team(session, user: User):
    team = Team(
        name='Time1',
        team_members=4,
        owner_id=user.id,
    )

    session.add(team)
    session.commit()
    session.refresh(team)

    user = session.scalar(select(User).where(User.id == user.id))

    assert team in user.teams


def test_create_invite(session, user: User, team: Team):
    invite = Invite(
        token='123456789abcdef',
        name='athlete1',
        email='athlete1@email.com',
        team=team.id,
        user_id=user.id,
    )

    session.add(invite)
    session.commit()
    session.refresh(invite)

    user = session.scalar(select(User).where(User.id == user.id))

    assert invite in user.invites


def test_create_race(session, user: User):
    race = Race(
        name='Race 1',
        place='anywhere',
        race_date=datetime.now(),
        distance=100,
        url_race='race1.com',
        race_description='description',
        place_description='description',
        observations='description',
        user_id=user.id,
    )
    session.add(race)
    session.commit()
    session.refresh(race)

    user = session.scalar(select(User).where(User.id == user.id))

    assert race in user.races
