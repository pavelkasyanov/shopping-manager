import pytest
from fastapi.testclient import TestClient

from shopping_manager.app import app


@pytest.fixture
def client():
    return TestClient(app)