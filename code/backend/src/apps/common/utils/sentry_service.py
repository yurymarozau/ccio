import logging

import sentry_sdk
from sentry_sdk import Scope


class SentryService:
    """Logger service for sentry"""

    @staticmethod
    def set_extras(scope: Scope, extras: dict = None) -> None:
        """Method to set additional attributes to sentry message"""
        if scope is None or extras is None:
            return

        for extra_key, extra_value in extras.items():
            scope.set_extra(extra_key, extra_value)

    @staticmethod
    def set_level(scope: Scope, level: int = logging.INFO) -> None:
        """Method to specify message level"""
        if scope is None:
            return

        scope.set_level(logging.getLevelName(level).lower())

    @classmethod
    def capture_message(cls, message: str = '', level: int = logging.INFO, extras: dict = None) -> None:
        """Method to capture custom info message and send to sentry"""
        with sentry_sdk.new_scope() as scope:
            cls.set_extras(scope, extras)
            cls.set_level(scope, level)
            sentry_sdk.capture_message(message=message)

    @classmethod
    def capture_exception(cls, error: BaseException, level: int = logging.ERROR, extras: dict = None) -> None:
        """Method to capture exception and send to sentry"""
        with sentry_sdk.new_scope() as scope:
            cls.set_extras(scope, extras)
            cls.set_level(scope, level)
            sentry_sdk.capture_exception(error=error)
