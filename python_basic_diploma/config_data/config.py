import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
DB_PATH = "database.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
URL_HIGH = os.getenv("URL_HIGH")
URL_LOW = os.getenv("URL_LOW")
ACCEPT = os.getenv("ACCEPT")
URL_CUSTOM_RU = os.getenv("URL_CUSTOM_RU")
URL_CUSTOM_USA = os.getenv("URL_CUSTOM_USA")
URL_CUSTOM_UK = os.getenv("URL_CUSTOM_UK")
URL_CUSTOM_FR = os.getenv("URL_CUSTOM_FR")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("high", " Топ 10 лучших по рейтингу Кинопоиск"),
    ("low", " Топ 10 худщих по рейтингу Кинопоиск"),
    ("custom", " Поиск фильма по старне"),
    ("history", "История послдених 10 запросов"),
)
