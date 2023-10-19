def test_create_team(client, user, token):
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


def test_get_user_teams(client, token, user, team):
    response = client.get(
        '/teams/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.json() == {
        'teams': [
            {
                'id': team.id,
                'name': team.name,
                'team_members': team.team_members,
            }
        ]
    }
