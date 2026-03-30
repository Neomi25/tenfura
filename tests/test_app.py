import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client) -> None:
    response = client.get('/')
    assert response.status_code == 200


def test_api_hello(client) -> None:
    response = client.get('/api/hello')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'message' in data


def test_not_found(client) -> None:
    response = client.get('/non-existent')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'Not found'
