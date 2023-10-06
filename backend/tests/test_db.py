from app.models import User
from sqlalchemy import select


def test_create_user(session):
    new_user = User(name='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.name == 'alice'))

    assert user.name == 'alice'
