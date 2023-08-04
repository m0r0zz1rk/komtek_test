import os
import environ

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

"""
    В зависимости от значения PROD в файле .env
    выбираем нужную конфигурацию проекта
"""

if env('START') == 'PROD':
    print('Server running in production\n')
    from .vars.prod import *
else:
    print('Server running in development\n')
    from .vars.dev import *
