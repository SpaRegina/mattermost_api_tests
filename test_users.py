import requests
from config import BASE_URL, USERNAME
from utils import get_token

def test_get_users():
    token = get_token()
    response = requests.get(
        f"{BASE_URL}/api/v4/users",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

def test_find_user_by_email():
    token = get_token()
    response = requests.get(
        f"{BASE_URL}/api/v4/users/email/{USERNAME}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == USERNAME
