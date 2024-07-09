def test_create_athlete(client, athlete, token):
    response = client.post(
        'api/v1/athletes/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'name': 'alice',
        'email': 'alice@example.com',
        'id': athlete.id + 2,
    }


def test_create_athlete_already_registered(client, athlete, token):
    response = client.post(
        'api/v1/athletes/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': athlete.name,
            'email': athlete.email,
            'password': athlete.password,
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        'detail': 'User already registered',
    }


def test_update_athlete(client, athlete, token):
    response = client.put(
        f'api/v1/athletes/{athlete.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'Athlete updated'}


def test_update_athlete_with_wrong_user(client, other_athlete, token):
    response = client.put(
        f'api/v1/athletes/{other_athlete.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_update_athlete_not_found(client):
    response = client.put(
        'api/v1/athletes/1',
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 401
    assert response.json() == {
        'detail': 'Not authenticated',
    }


def test_delete_athlete(client, athlete, token):
    response = client.delete(
        'api/v1/athletes/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'Athlete deleted'}


def test_delete_athlete_not_found(client):
    response = client.delete('api/v1/athletes')

    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}
