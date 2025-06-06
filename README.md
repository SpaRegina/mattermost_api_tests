# Mattermost API Тесты

Проект автоматизированного тестирования API Mattermost с использованием `pytest` и `requests`.

## 🔧 Установки

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SpaRegina/mattermost_api_tests.git
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` на основе шаблона `.env.example`:
   ```bash
   cp .env.example .env  # или создайте вручную в Windows
   ```
   Укажите в нём реальные значения переменных:
   ```env
   BASE_URL="http://localhost:8065"
   EMAIL="your_email@example.com"
   PASSWORD="your_password"
   TEAM_NAME="your_team_name"
   CHANNEL_NAME="your_channel_id"
   ```

## 🚀 Запуск тестов

```bash
pytest -v
```

Для генерации HTML-отчёта о тестировании:

```bash
pytest --html=report.html --self-contained-html
```

После выполнения появится файл report.html, который можно открыть в браузере.

## 🧚 Покрытие

Проверяются следующие сценарии:

### test_auth.py
- Валидная авторизация (и проверка наличия `id`, `roles` в ответе)
- Невалидная авторизация
- Попытка входа с заблокированной учёткой
- Попытка входа с неактивированной учёткой
- Обработка недоступности сервера

### test_channels.py
- Создание публичного канала
- Создание канала с уже существующим именем (ожидается 400/409)

### test_messages.py
- Отправка сообщения в канал
- Получение сообщений из канала по ID

### test_users.py
- Получение списка пользователей
- Поиск пользователя по email (GET /users/email/{email})

## 📃 Структура проекта

```
mattermost_api_tests/
├── .env.example
├── config.py
├── conftest.py
├── requirements.txt
├── test_auth.py
├── test_channels.py
├── test_messages.py
├── test_users.py
└── utils.py
```

---

✅ Проект поддерживается для локального тестирования Mattermost API.
