from datetime import datetime, time

from sqlalchemy import select

from app import models


def test_create_user(session):
    new_user = models.User(name='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(
        select(models.User).where(models.User.name == 'alice')
    )

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


def test_create_invite(
    session, user: models.User, team: models.Team, race: models.Race
):
    invite = models.Invite(
        token='123456789abcdef',
        name='athlete1',
        email='athlete1@email.com',
        team_id=team.id,
        race_id=race.id,
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


def test_create_equipaments_athlete(
    session, user: models.User, equipament: models.Equipaments
):
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

    query = session.scalar(
        select(models.EquipamentsAthlete).where(
            models.EquipamentsAthlete.user_id == user.id
        )
    )

    assert query == equipaments_athlete


def test_create_equipaments(session, race: models.Race):
    equipaments = models.Equipaments(
        quantity=2,
        modality='bike',
        race_id=race.id,
    )

    session.add(equipaments)
    session.commit()
    session.refresh(equipaments)

    query = session.scalar(
        select(models.Equipaments).where(
            models.Equipaments.race_id == race.id
        )
    )

    assert query == equipaments


def test_create_fugleman(session, race: models.Race):
    fugleman = models.Fugleman(
        name='organizador',
        email='org@mail.com',
        phone='99999999999',
        race_id=race.id,
    )

    session.add(fugleman)
    session.commit()
    session.refresh(fugleman)

    query = session.scalar(
        select(models.Fugleman).where(
            models.Fugleman.race_id == race.id
        )
    )

    assert query == fugleman


def test_create_strategic_planning(session, user: models.User, race: models.Race):
    strategic_planning = models.StrategicPlanning(
        mission='mission',
        vision='vision',
        values='values',
        strategic_objectives='strategic_objectives',
        immediate_objectives='immediate_objectives',
        strengths='strengths',
        weaknesses='weaknesses',
        opportunities='opportunities',
        threats='threats',

        race_id=race.id,
        user_id=user.id,
    )

    session.add(strategic_planning)
    session.commit()
    session.refresh(strategic_planning)

    query = session.scalar(
        select(models.StrategicPlanning).where(
            models.StrategicPlanning.user_id == user.id
        )
    )

    assert query == strategic_planning


def test_create_user_race(session, user: models.User, race: models.Race):
    user_race = models.TeamRace(
        race_id=race.id,
        user_id=user.id,
    )

    session.add(user_race)
    session.commit()
    session.refresh(user_race)

    query = session.scalar(
        select(models.TeamRace).where(
            models.TeamRace.user_id == user.id,
            models.TeamRace.race_id == race.id
        )
    )

    assert query == user_race


def test_create_time_line(session, race: models.Race):
    user_race = models.TimeLine(
        stage='AT1',
        distance=23,
        estimated_time=datetime.now().time(),
        observations='observations',
        previous_stage=None,
        next_stage=None,        
        race_id=race.id,
    )

    session.add(user_race)
    session.commit()
    session.refresh(user_race)

    query = session.scalar(
        select(models.TimeLine).where(
            models.TimeLine.race_id == race.id
        )
    )

    assert query == user_race
