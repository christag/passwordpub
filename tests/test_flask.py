import pytest

from start_server import create_app

@pytest.fixture
def client():
    app = create_app()
    app.debug = True
    yield app.test_client()

def test_flask(client):
    rv = client.get('/api')
    assert rv.status_code == 200