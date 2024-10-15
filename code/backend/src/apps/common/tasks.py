from abc import abstractmethod

from celery import Task

from config.settings import celery_app


class MetaTask(type):
    """Metaclass to register tasks manually due to disabled auto task register in celery>=5"""
    def __new__(mcs, *args, **kwargs):
        task = super().__new__(mcs, *args, **kwargs)
        task.name = f'{task.__module__}.{task.__name__}'
        celery_app.register_task(task)
        return task


class BaseTask(Task, metaclass=MetaTask):
    """Base class for celery tasks with MetaTask metaclass."""
    abstract = True

    @abstractmethod
    def custom_run(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        try:
            return self.custom_run(*args, **kwargs)
        except Exception as exc:
            raise exc
            raise self.retry(exc=exc)
