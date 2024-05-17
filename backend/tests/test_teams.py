def test_create_team(client, token, race, athlete):
    payload = expected = {
        'name': 'Time1',
        'team_members': 2,
        'race_id': race.id,
        'logo': 'null',
    }

    response = client.post(
        'api/v1/teams/',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    expected.update(id=1)
    assert response.json() == expected


def test_get_athlete_teams(client, token, team, race):
    response = client.get(
        'api/v1/teams/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.json() == [
        {
            'id': team.id,
            'name': team.name,
            'team_members': team.team_members,
            'logo': None,
            'race_id': race.id,
        }
    ]
