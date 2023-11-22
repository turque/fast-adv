from sqlalchemy import select

from app.models import Invite


def test_create_invite(session, client, token, team, race, mocker):
    mocker.patch('app.api.v1.endpoints.invites.send_email', return_value=True)

    response = client.post(
        'api/v1/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'guest1',
            'email': 'guest1@mail.com',
            'team': team.id,
            'race': race.id,
        },
    )

    invite = session.scalar(select(Invite))

    assert invite.sent_at is not None
    assert response.status_code == 201


def test_create_invite_not_sent(session, client, token, team, race, mocker):
    mocker.patch('app.api.v1.endpoints.invites.send_email', return_value=False)

    response = client.post(
        'api/v1/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'guest1',
            'email': 'guest1@mail.com',
            'team': team.id,
            'race': race.id,
        },
    )

    invite = session.scalar(select(Invite))

    assert invite.sent_at is None
    assert response.status_code == 201


def test_create_invite_without_parameters(client, token, team):
    response = client.post(
        'api/v1/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'email': 'guest1@mail.com', 'team': team.id},
    )

    assert response.status_code == 422
    response = client.post(
        'api/v1/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'name': 'guest1', 'team': team.id},
    )

    assert response.status_code == 422


def test_create_invite_with_invalid_team_id(client, token, other_team, race):
    response = client.post(
        'api/v1/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'guest1',
            'email': 'guest1@mail.com',
            'team': other_team.id,
            'race': race.id,
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Invalid or nonexistent team'}
