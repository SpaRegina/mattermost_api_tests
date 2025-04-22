import pytest
import requests
from config import BASE_URL, USERNAME, PASSWORD


@pytest.fixture(scope="session")
def auth_headers():
    """Фикстура для получения заголовков авторизации с токеном"""
    url = f"{BASE_URL}/api/v4/users/login"
    response = requests.post(url, json={"login_id": USERNAME, "password": PASSWORD})
    assert response.status_code == 200, "Не удалось авторизоваться"

    token = response.headers.get("Token") or response.json().get("token")
    assert token, "Токен не найден в ответе"

    return {"Authorization": f"Bearer {token}"}
