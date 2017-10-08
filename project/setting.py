# coding: utf-8
"""Config settings for the Telegram Bot."""
from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent

YANDEX_API_USER = config('YANDEX_API_USER')
YANDEX_API_KEY = config('YANDEX_API_KEY')
