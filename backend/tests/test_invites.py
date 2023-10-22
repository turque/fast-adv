def test_create_invite(client, token, team):
    response = client.post(
        '/invite/create',
        headers={'Authorization': f'Bearer {token}'},
        json={'name': 'guest1', 'email': 'guest1@mail.com', 'team': team.id},
    )

    assert response.status_code == 201
