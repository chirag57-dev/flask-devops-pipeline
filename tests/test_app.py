import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert response.get_json() == {'items': ['item1', 'item2', 'item3']}
    
def test_create_item_no_body(client):
    response = client.post('/items')
    assert response.status_code == 400
    assert response.get_json() == {'message': 'Invalid data'}
    

def test_create_item_valid(client):
    response = client.post('/items', json={'name': 'item4'})
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Item created', 'data': {'name': 'item4'}}