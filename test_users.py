import requests
from config import BASE_URL, USERNAME, PASSWORD

def get_token():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": USERNAME, "password": PASSWORD}
    )
    assert response.status_code == 200, "Не удалось авторизоваться"
    return response.json().get("token") or response.headers.get("Token")

def test_get_users():
    token = get_token()
    response = requests.get(
        f"{BASE_URL}/api/v4/users",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
