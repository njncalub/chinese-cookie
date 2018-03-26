import pytest
from apistar.test import TestClient

from app import app


HTTP_HEADERS = {b'Content-Type': b'application/json'}


@pytest.fixture
def random_fortune():
    client = TestClient(app)
    
    # HACK: get a random fortune first
    # as we do not have access to the db session for now
    response = client.get('/fortunes/random')
    
    # test if dict has keys
    assert 'uuid' in response.json()
    assert 'message' in response.json()
    
    return response.json()

def test_list_fortunes():
    """
    Testing list_fortunes using TestClient.
    """
    
    client = TestClient(app)
    response = client.get('/fortunes/')
    
    assert response.status_code == 200
    
    fortune = response.json()
    
    import collections
    assert isinstance(fortune, collections.Sequence)
    assert not isinstance(fortune, str)

def test_create_fortune():
    """
    Testing list_fortunes using TestClient.
    """
    
    client = TestClient(app)
    sample_message = 'Sample POST Message'
    response = client.post(f'/fortunes/?message={sample_message}',
                           headers=HTTP_HEADERS)
    
    assert response.status_code == 201
    
    # test if dict has keys
    # BUG: response not returning proper values so the tests below will fail.
    assert b'uuid' in response.json()
    assert b'message' in response.json()
    
    # test if same
    assert response.json()['message'] == sample_message
    
    # TODO:
    # implement DELETE method to delete the created fortune

def test_get_fortune(random_fortune):
    """
    Testing get_fortune using TestClient.
    """
    
    client = TestClient(app)
    response = client.get(f"/fortunes/{random_fortune['uuid']}")
    
    assert response.status_code == 200
    
    # test if dict has keys
    assert 'uuid' in response.json()
    assert 'message' in response.json()
    
    # test if the same
    fortune = response.json()
    assert random_fortune['uuid'] == fortune['uuid']
    assert random_fortune['message'] == fortune['message']

def test_update_fortune(random_fortune):
    """
    Testing get_fortune using TestClient.
    """
    
    client = TestClient(app)
    sample_message = 'Sample PATCH Message'
    response = client.patch(
        f"/fortunes/{random_fortune['uuid']}?message={sample_message}",
        headers=HTTP_HEADERS
    )
    
    assert response.status_code == 200
    
    # test if dict has keys
    assert 'uuid' in response.json()
    assert 'message' in response.json()
    
    # test if the same
    fortune = response.json()
    assert random_fortune['uuid'] == fortune['uuid']
    assert fortune['message'] == sample_message
    
    # disabled for now as it might introduce unwanted results
    # e.g. what if same message before and after?
    # assert random_fortune['message'] != fortune['message']

def test_get_random_fortune():
    """
    Testing get_random_fortune using TestClient.
    """
    
    client = TestClient(app)
    response = client.get('/fortunes/random')
    
    assert response.status_code == 200
    
    # test if dict has keys
    assert 'uuid' in response.json()
    assert 'message' in response.json()
