import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = config('ENVIRONMENT')

ENABLE_DOCS = config('ENABLE_DOCS', default=False, cast=bool)
