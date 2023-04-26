def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/rates/')
    assert response.status_code == 200


def test_pots_api_rate_list(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }
