import requests
from config import BASE_URL
from utils import get_token, get_team_id, get_channel_id

def test_send_message():
    token = get_token()
    team_id = get_team_id(token)
    channel_id = get_channel_id(token, team_id)
    headers = {"Authorization": f"Bearer {token}"}
    post = requests.post(
        f"{BASE_URL}/api/v4/posts",
        headers=headers,
        json={
            "channel_id": channel_id,
            "message": "Hello from automated test!"
        }
    )
    assert post.status_code == 201
