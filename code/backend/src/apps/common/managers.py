from django.db import models

from apps.common.querysets import HardDeleteQuerySet, SoftDeleteQuerySet


class HardDeleteManager(models.Manager):
    def get_queryset(self):
        return HardDeleteQuerySet(self.model, using=self._db)

    def restore(self):
        return self.get_queryset().restore()

    def alive(self):
        return self.get_queryset().alive()

    def deleted(self):
        return self.get_queryset().deleted()


class SoftDeleteManager(HardDeleteManager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()

    def delete(self):
        return self.get_queryset().delete()

    def hard_delete(self):
        return super().get_queryset().delete()
