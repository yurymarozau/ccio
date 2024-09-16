import os

from decouple import config

from config.settings.common import BASE_DIR

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = config('AWS_SES_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN')

USE_ENCRYPTED_S3_STORAGE = True

STATIC_DIR = 'static'
MEDIA_DIR = 'media'

AWS_STATIC_LOCATION = 'static'

PUT_STATIC_TO_S3 = config('PUT_STATIC_TO_S3', default=False, cast=bool)

STORAGES = {
    'default': {
        'BACKEND': 'config.storages.MediaStorage'
            if PUT_STATIC_TO_S3
            else 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'config.storages.StaticStorage'
            if PUT_STATIC_TO_S3
            else 'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}

if PUT_STATIC_TO_S3:
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
else:
    STATIC_URL = f"/{STATIC_DIR}/"
    STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir, STATIC_DIR))

    MEDIA_URL = f"/{MEDIA_DIR}/"
    MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir, MEDIA_DIR))

STATICFILES_DIRS = (
)
