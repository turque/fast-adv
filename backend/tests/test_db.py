from sqlalchemy import select

from api.models import Team, User


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
