def test_create_team(client, token, race):
    response = client.post(
        'api/v1/teams/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Time1',
            'team_members': 2,
            'race_id': race.id,
            'logo': 'null',
        },
    )

    assert response.json() == {
        'id': 1,
        'name': 'Time1',
        'team_members': 2,
        'race_id': race.id,
    }


def test_get_athlete_teams(client, token, team, race):
    response = client.get(
        'api/v1/teams/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.json() == {
        'teams': [
            {
                'id': team.id,
                'name': team.name,
                'team_members': team.team_members,
                'race_id': race.id,
            }
        ]
    }
