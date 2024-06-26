from freezegun import freeze_time


def test_get_token(client, athlete):
    response = client.post(
        'api/v1/auth/token',
        data={'username': athlete.email, 'password': athlete.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_invalid_athlete(client):
    response = client.post(
        'api/v1/auth/token',
        data={'username': 'test', 'password': 'test'},
    )
    response.json()

    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_invalid_password(client, athlete):
    response = client.post(
        'api/v1/auth/token',
        data={'username': athlete.email, 'password': 'wrong_pass'},
    )
    response.json()

    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_refresh_token(client, athlete, token):
    response = client.post(
        'api/v1/auth/refresh_token',
        headers={'Authorization': f'Bearer {token}'},
    )

    data = response.json()

    assert response.status_code == 200
    assert 'access_token' in data
    assert 'token_type' in data
    assert response.json()['token_type'] == 'bearer'


def test_token_expiry(client, athlete):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            'api/v1/auth/token',
            data={
                'username': athlete.email,
                'password': athlete.clean_password,
            },
        )
        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2023-07-14 12:31:00'):
        response = client.post(
            'api/v1/auth/refresh_token',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == 401
        assert response.json() == {'detail': 'Could not validate credentials'}
