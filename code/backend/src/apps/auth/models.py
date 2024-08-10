from django.db import models

from apps.common.models import AbstractBaseModel


class Wallet(AbstractBaseModel):
    public_address = models.CharField(
        verbose_name='Web3 Wallet public address',
        max_length=42 # max length of EVM-compatible wallet address (0x + 40 chars)
    )
