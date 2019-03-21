import pytest

from start_server import create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    return app.test_client()