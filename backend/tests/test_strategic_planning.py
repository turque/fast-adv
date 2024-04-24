from app import schemas

payload = {
    'mission': 'string',
    'vision': None,
    'values': None,
    'strategic_objectives': 'string',
    'immediate_objectives': 'string',
    'strengths': 'string',
    'weaknesses': 'string',
    'opportunities': 'string',
    'threats': 'string',
}


def test_get_strategics_by_race(client, token, race, strategic_planning):

    strategic_schema = schemas.StrategicPlanning.model_validate(
        strategic_planning
    ).model_dump()

    response = client.get(
        f'api/v1/strategic/{race.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert strategic_schema == response.json()[0]
    assert response.status_code == 200


def test_create_strategic_planning(client, athlete, token, race):
    expected = payload
    expected.update(
        {
            'race_id': race.id,
            'athlete_id': athlete.id,
            'id': 1,
        }
    )

    response = client.post(
        f'api/v1/strategic/?race_id={race.id}',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.json() == expected
    assert response.status_code == 201


def test_try_create_with_strategic_planning_already_registered(
    client, athlete, token, race, strategic_planning
):
    expected = {
        'detail': ('Athlete has already registered strategic planning')
    }
    response = client.post(
        f'api/v1/strategic/?race_id={race.id}',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.json() == expected
    assert response.status_code == 400


def test_update_strategic_planning(
    client, athlete, token, race, strategic_planning
):
    payload = schemas.StrategicPlanning.model_validate(
        strategic_planning
    ).model_dump()
    payload['mission'] = 'Altered'

    response = client.put(
        f'api/v1/strategic/{strategic_planning.id}',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.status_code == 200
    assert response.json().get('mission') == 'Altered'
