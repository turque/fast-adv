from datetime import datetime

from sqlalchemy import select

from app import models


def test_create_user(session):
    new_user = models.User(name='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(models.User).where(models.User.name == 'alice'))

    assert user.name == 'alice'


def test_create_team(session, user: models.User, race: models.Race):
    team = models.Team(
        name='Time1', team_members=4, owner_id=user.id, race_id=race.id
    )

    session.add(team)
    session.commit()
    session.refresh(team)

    user = session.scalar(select(models.User).where(models.User.id == user.id))

    assert team in user.teams


def test_create_invite(session, user: models.User, team: models.Team, race: models.Race):
    invite = models.Invite(
        token='123456789abcdef',
        name='athlete1',
        email='athlete1@email.com',
        team=team.id,
        race=race.id,
        user_id=user.id,
    )

    session.add(invite)
    session.commit()
    session.refresh(invite)

    user = session.scalar(select(models.User).where(models.User.id == user.id))

    assert invite in user.invites


def test_create_race(session, user: models.User):
    race = models.Race(
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

    user = session.scalar(select(models.User).where(models.User.id == user.id))

    assert race in user.races


def test_create_equipaments_athlete(session, user: models.User, equipament: models.Equipaments):
    equipaments_athlete = models.EquipamentsAthlete(
        observations='New equipament',
        have=True,
        ready=False,
        user_id=user.id,
        equipament_id=equipament.id,
    )

    session.add(equipaments_athlete)
    session.commit()
    session.refresh(equipaments_athlete)

def test_create_equipaments(session):
    pass


def test_create_fugleman(session):
    pass


def test_create_strategic_planning(session):
    pass


def test_create_user_race(session):
    pass


def test_create_time_line(session):
    pass
