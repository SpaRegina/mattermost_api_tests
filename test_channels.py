import requests
import uuid
from config import BASE_URL
from utils import get_token, get_team_id

def test_create_channel():
    token = get_token()
    team_id = get_team_id(token)
    response = requests.post(
        f"{BASE_URL}/api/v4/channels",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "team_id": team_id,
            "name": f"testchannel-{uuid.uuid4().hex[:6]}",
            "display_name": "Test Channel",
            "type": "O"
        }
    )
    assert response.status_code == 201

def test_create_duplicate_channel():
    token = get_token()
    team_id = get_team_id(token)
    name = f"duplicate-test-{uuid.uuid4().hex[:6]}"
    # Первое создание
    requests.post(
        f"{BASE_URL}/api/v4/channels",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "team_id": team_id,
            "name": name,
            "display_name": "Duplicate Test",
            "type": "O"
        }
    )
    # Повторное создание
    response = requests.post(
        f"{BASE_URL}/api/v4/channels",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "team_id": team_id,
            "name": name,
            "display_name": "Duplicate Test",
            "type": "O"
        }
    )
    assert response.status_code in [400, 409]
