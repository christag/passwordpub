import pytest

from start_server import create_app
from bar_kit import ops_manual

@pytest.fixture
def client():
    bar = ops_manual.open_bar()
    app = create_app(bar)
    app.debug = True
    yield app.test_client()

def test_flask(client):
    rv = client.get('/api')
    assert rv.status_code == 200