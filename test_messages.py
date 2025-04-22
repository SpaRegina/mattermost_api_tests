import requests
from config import BASE_URL
from utils import get_token, get_channel_id

def test_send_message():
    token = get_token()
    channel_id = get_channel_id(token)
    response = requests.post(
        f"{BASE_URL}/api/v4/posts",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "channel_id": channel_id,
            "message": "Hello from Pytest!"
        }
    )
    assert response.status_code == 201

def test_get_messages_from_channel():
    token = get_token()
    channel_id = get_channel_id(token)
    response = requests.get(
        f"{BASE_URL}/api/v4/channels/{channel_id}/posts",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "posts" in data
