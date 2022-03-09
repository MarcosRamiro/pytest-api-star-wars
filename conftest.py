from pytest import fixture
import requests
import json
import os


headers = {
    'Authorization': 'Bearer sdfgdkgjsgsjdlsdfkljdk',
    'x-bla': 'bla'
}


@fixture(scope='session')
def environment():
    try:
        url = os.getenv('URL_STAR_WARS', 'https://swapi.dev/api/people/1')
        client_id = os.getenv('CLIENT_ID', 'minha_client_id')
        client_secret = os.getenv('CLIENT_SECRET', 'minha_client_secret')
        yield url, client_id, client_secret
    finally:
        print('fim do metodo environment fixture')


@fixture(scope='session')
def token(environment):
    """call sts to generate token"""
    return "fake_token"


@fixture
def url(environment):
    return environment[0]


@fixture
def get_api_star_wars_people_one(url, token):
    headers.update({'Authorization': f'Bearer {token}'})
    resposta_api = requests.get(url, headers=headers)
    resposta_api.raise_for_status()
    resposta_json = resposta_api.json()
    return resposta_json

