from dotenv import load_dotenv, find_dotenv
import os

# Конфиденциальные данные
load_dotenv(find_dotenv())  # погрузка .env
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_PORT_OUT = os.getenv('DB_PORT_OUT')
DB_HOST = os.getenv('DB_HOST')
DEBUG_MODE = os.getenv('DEBUG_MODE', False)
TESTING_MODE = os.getenv('TESTING_MODE', False)


class Config(object):
    DEBUG = DEBUG_MODE
    TESTING = TESTING_MODE
    CSRF_TRUSTED_ORIGINS = []

    DATABASES_CONFIG_DICT = \
        {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': DB_NAME,
                'USER': DB_USER,
                'PASSWORD': DB_PASSWORD,
                'HOST': DB_HOST,
                'PORT': DB_PORT,
                "TEST": {
                    "NAME": "mytestdatabase",
                },
            }
        }
