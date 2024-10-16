from celery import Celery
from celery.schedules import crontab
from decouple import config

celery_app = Celery(config('APP_NAME'))


class Config:
    enable_utc = True
    timezone = 'UTC'
    broker_url = f'redis://{config("REDIS_HOST")}:{config("REDIS_PORT")}/{config("BROKER_DB")}'
    result_backend = 'django-db'
    result_serializer = 'json'
    result_extended = True
    result_expires = None
    accept_content = ('json',)
    broker_connection_retry_on_startup = True
    task_track_started = True
    task_serializer = 'json'

    task_default_queue = 'general'
    task_routes = {
        'apps.chains.tasks.UpdateChainsListTask': {'queue': 'general'},
        'apps.chains.tasks.UpdateTokensTask': {'queue': 'general'},
    }

    imports = (
        'apps.chains.tasks',
    )

    beat_schedule = {
        'apps.chains.tasks.UpdateChainsListTask': {
            'task': 'apps.chains.tasks.UpdateChainsListTask',
            'schedule': crontab(minute='0', hour='0')
        },
    }


celery_app.config_from_object(Config)
