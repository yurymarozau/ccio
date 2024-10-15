import logging

import sentry_sdk
from decouple import config
from sentry_sdk.integrations.celery import \
    CeleryIntegration as SentryCeleryIntegration
from sentry_sdk.integrations.django import \
    DjangoIntegration as SentryDjangoIntegration
from sentry_sdk.integrations.logging import \
    LoggingIntegration as SentryLoggingIntegration

if config('USE_SENTRY', default=False, cast=bool):
    sentry_sdk.init(
        dsn=config('SENTRY_DSN'),
        integrations=[
            SentryCeleryIntegration(),
            SentryDjangoIntegration(),
            SentryLoggingIntegration(
                level=logging.INFO,
                event_level=logging.ERROR
            ),
        ],
        send_default_pii=True,
        environment=config('ENVIRONMENT'),
        traces_sample_rate=1.0,
    )
