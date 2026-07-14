import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as app_activities

BASE_ACTIVITIES = copy.deepcopy(app_activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_activities.clear()
    app_activities.update(copy.deepcopy(BASE_ACTIVITIES))
    yield
    app_activities.clear()
    app_activities.update(copy.deepcopy(BASE_ACTIVITIES))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
