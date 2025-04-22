from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:8065")
USERNAME = os.getenv("EMAIL", "admin@example.com")
PASSWORD = os.getenv("PASSWORD", "Admin123!")
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "123")  # имя канала
TEAM_NAME = os.getenv("TEAM_NAME", "mattermost-test-org")  # имя команды
