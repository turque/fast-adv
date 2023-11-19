def test_create_invite(client, token, mocker):
    mocker.patch('app.api.v1.endpoints.utils.send_test_email')

    response = client.post(
        'api/v1/utils/test-email/',
        headers={'Authorization': f'Bearer {token}'},
        params={'email_to': 'test@mail.com'},
    )

    assert response.status_code == 201
    assert response.json() == {'detail': 'Test email sent'}
