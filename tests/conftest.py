from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

BASE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    """Reset in-memory activity data before each test for isolation."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASE_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
