def test_create_invite(client, token, team, mocker):
    mock_SMTP = mocker.MagicMock(name='app.services.smtp.smtplib.SMTP')
    mocker.patch('app.services.smtp.smtplib.SMTP', new=mock_SMTP)

    response = client.post(
        '/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'name': 'guest1', 'email': 'guest1@mail.com', 'team': team.id},
    )

    assert response.status_code == 201


def test_create_invite_without_parameters(client, token, team):
    response = client.post(
        '/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'email': 'guest1@mail.com', 'team': team.id},
    )

    assert response.status_code == 422
    response = client.post(
        '/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'name': 'guest1', 'team': team.id},
    )

    assert response.status_code == 422


def test_create_invite_with_invalid_team_id(client, token, other_team):
    response = client.post(
        '/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'guest1',
            'email': 'guest1@mail.com',
            'team': other_team.id,
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Invalid or absent team'}
