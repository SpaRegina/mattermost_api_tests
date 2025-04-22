import requests
from config import BASE_URL, USERNAME, PASSWORD, TEAM_NAME, CHANNEL_NAME

def get_token():
    response = requests.post(
        f"{BASE_URL}/api/v4/users/login",
        json={"login_id": USERNAME, "password": PASSWORD}
    )
    if response.status_code != 200:
        raise Exception("Не удалось получить токен")
    return response.headers.get("Token")

def get_team_id(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/v4/teams", headers=headers)
    for team in response.json():
        if team["name"] == TEAM_NAME:
            return team["id"]
    raise Exception(f"Команда '{TEAM_NAME}' не найдена")

def get_channel_id(token, team_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/api/v4/teams/{team_id}/channels", headers=headers)
    for channel in response.json():
        if channel["name"] == CHANNEL_NAME:
            return channel["id"]
    raise Exception(f"Канал '{CHANNEL_NAME}' не найден в команде")
