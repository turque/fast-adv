def test_create_race_with_minimal_fields(client, athlete, token, race):
    payload = expected = {
        'name': race.name,
        'place': None,
        'race_date': None,
        'distance': None,
        'url_race': None,
        'race_description': None,
        'place_description': None,
        'observations': None,
    }

    expected.update({'id': race.id + 1})

    response = client.post(
        'api/v1/races/',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.status_code == 201
    assert response.json() == expected


def test_create_race_with_all_fields(client, athlete, token, race):
    payload = expected = {
        'name': race.name,
        'place': race.place,
        'race_date': race.race_date.strftime('%Y-%m-%d'),
        'distance': race.distance,
        'url_race': race.url_race,
        'race_description': race.race_description,
        'place_description': race.place_description,
        'observations': race.observations,
    }

    expected.update({'id': race.id + 1})

    response = client.post(
        'api/v1/races/',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.status_code == 201
    assert response.json() == expected


def test_update_race(client, athlete, token, race):
    payload = {
        'name': 'altered name',
        'place': None,
        'race_date': None,
        'distance': None,
        'url_race': None,
        'race_description': None,
        'place_description': None,
        'observations': None,
    }

    response = client.put(
        f'api/v1/races/{race.id}',
        headers={'Authorization': f'Bearer {token}'},
        json=payload,
    )

    assert response.status_code == 200
    assert response.json().get('name') == 'altered name'


def test_get_races(client, token, race):
    response = client.get(
        'api/v1/races/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert race.name == response.json()[0].get('name')


def test_get_race_by_id(client, token, race):
    response = client.get(
        f'api/v1/races/{race.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert race.name == response.json().get('name')


def test_delete_race_by_id(client, token, race):
    delete_response = client.delete(
        f'api/v1/races/{race.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert delete_response.status_code == 200
