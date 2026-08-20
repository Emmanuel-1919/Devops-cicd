import os

os.environ["APP_ENV"] = "dev"
os.environ["GIT_BRANCH"] = "develop"
os.environ["GIT_COMMIT"] = "abc1234567"
os.environ["APP_VERSION"] = "1.0.0"

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_index_contains_env():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"DEV" in response.data
    assert b"abc1234" in response.data
