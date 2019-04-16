# Import modules
import pytest

from start_server import create_app
from bar_kit import ops_manual

# Create a fixture - an instance of the bar opened in Flask.
@pytest.fixture
def client():
    bar = ops_manual.open_bar()
    app = create_app(bar)
    app.debug = True
    yield app.test_client()