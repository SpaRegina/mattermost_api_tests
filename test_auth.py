import requests
import pytest
from config import BASE_URL, USERNAME, PASSWORD
from unittest.mock import patch

def test_valid_login():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": USERNAME, "password": PASSWORD}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "roles" in data

def test_invalid_login():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": "wrong", "password": "wrong"}
    )
    assert response.status_code == 401

def test_blocked_user_login():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": "blocked@example.com", "password": "Blocked123!"}
    )
    assert response.status_code == 403
    assert "user has been deactivated" in response.text.lower()

def test_inactive_user_login():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": "inactive@example.com", "password": "Inactive123!"}
    )
    assert response.status_code == 403
    assert "account is not confirmed" in response.text.lower()

def test_auth_server_unavailable():
    with patch("requests.post", side_effect=requests.exceptions.ConnectionError):
        with pytest.raises(requests.exceptions.ConnectionError):
            requests.post(
                f"{BASE_URL}/api/v4/users/login",
                json={"login_id": "admin@example.com", "password": "Admin123!"}
            )
