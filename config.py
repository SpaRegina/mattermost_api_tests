from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("EMAIL")  # Используем EMAIL как имя пользователя
PASSWORD = os.getenv("PASSWORD")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")
TEAM_NAME = os.getenv("TEAM_NAME")
