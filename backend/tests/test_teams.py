def test_create_team(client, token):
    response = client.post(
        '/teams/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Time1',
            'team_members': 2,
        },
    )

    assert response.json() == {
        'id': 1,
        'name': 'Time1',
        'team_members': 2,
    }
