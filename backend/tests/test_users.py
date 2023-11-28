from app.schemas import UserPublic


def test_create_user(client, user, token):
    response = client.post(
        'api/v1/users/',
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
        'id': user.id + 1,
    }


def test_create_user_already_registered(client, user, token):
    response = client.post(
        'api/v1/users/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': user.name,
            'email': user.email,
            'password': user.password,
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        'detail': 'Username already registered',
    }


def test_read_users(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get(
        'api/v1/users/', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'api/v1/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'name': 'bob',
        'email': 'bob@example.com',
        'id': user.id,
    }


def test_update_user_with_wrong_user(client, other_user, token):
    response = client.put(
        f'api/v1/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_update_user_not_found(client):
    response = client.put(
        'api/v1/users/1',
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


def test_delete_user(client, user, token):
    response = client.delete(
        f'api/v1/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('api/v1/users/1')

    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_delete_user_wrong_user(client, other_user, token):
    response = client.delete(
        f'api/v1/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}
