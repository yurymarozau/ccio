from django.db import models
from django.utils import timezone


class HardDeleteQuerySet(models.QuerySet):
    def restore(self):
        return super().update(deleted_at=None)

    def alive(self):
        return self.filter(deleted_at=None)

    def deleted(self):
        return self.exclude(deleted_at=None)


class SoftDeleteQuerySet(HardDeleteQuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()
