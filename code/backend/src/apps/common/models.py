import uuid

from django.db import models
from django.utils import timezone

from apps.common.managers import HardDeleteManager, SoftDeleteManager


class AbstractUUIDModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AbstractSoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True)

    objects = SoftDeleteManager()
    objects_all = HardDeleteManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])


class AbstractBaseModel(AbstractSoftDeleteModel, AbstractUUIDModel):
    class Meta:
        abstract = True
