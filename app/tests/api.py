from currency.models import Source
from tests.utils import get_access_token


def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/rates/')
    assert response.status_code == 200


def test_post_api_rate_list(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_authenticate(api_client):

    token_response = get_access_token(api_client)

    assert token_response.status_code == 200


def test_get_token(api_client):

    token_response = get_access_token(api_client)

    assert 'access' in token_response.data
    assert 'refresh' in token_response.data


def test_get_api_source_list(api_client):

    token_response = get_access_token(api_client)
    token = token_response.json()['access']

    # request with token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get('/v1/api/currency/sources/')
    assert response.status_code == 200


def test_get_api_source(api_client):

    token_response = get_access_token(api_client)
    token = token_response.json()['access']
    source = Source.objects.last()

    # request with token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.get(f'/v1/api/currency/sources/{source.pk}/')
    assert response.status_code == 200


def test_delete_api_source(api_client):

    token_response = get_access_token(api_client)
    token = token_response.json()['access']
    source = Source.objects.last()

    # request with token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = api_client.delete(f'/v1/api/currency/sources/{source.pk}/')
    assert response.status_code == 204
    assert not Source.objects.filter(pk=source.pk).exists()


def test_create_api_source(api_client):

    new_source = {
        'name': 'New Source',
        'code_name': 'source',
        'source_url': 'https://newsource.com',
        'address': 'address',
        'phone': '000',
    }

    token_response = get_access_token(api_client)
    # Authenticate and obtain token
    token = token_response.json()['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Create new source
    response = api_client.post('/v1/api/currency/sources/', new_source)
    assert response.status_code == 201

    # Check that the source was created
    assert Source.objects.filter(name='New Source').exists()


def test_put_api_source(api_client):

    source = Source.objects.last()

    # authentication
    token_response = get_access_token(api_client)
    token = token_response.json()['access']

    url = f'/v1/api/currency/sources/{source.pk}/'
    data = {'name': 'Updated Source Name',
            'code_name': f'{source.code_name}',
            'source_url': 'https://newsource.com',
            'address': f'{source.address}',
            'phone': f'{source.phone}'
            }

    response = api_client.put(url, data, format='json', HTTP_AUTHORIZATION=f'Bearer {token}')
    assert response.status_code == 200

    source.refresh_from_db()
    assert source.name == 'Updated Source Name'
