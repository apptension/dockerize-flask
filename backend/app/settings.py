import os


config_names = ['POSTGRES_DB', 'POSTGRES_USER', 'POSTGRES_PASSWORD',
                'DB_SERVICE', 'DB_PORT']
DB_CONFIG = {name: os.environ.get(name) for name in config_names}

DB_URL = ('postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
          '{DB_SERVICE}:{DB_PORT}/{POSTGRES_DB}')
SQLALCHEMY_DATABASE_URI = DB_URL.format(**DB_CONFIG)

DEBUG = int(os.environ.get('DEBUG', '0'))
