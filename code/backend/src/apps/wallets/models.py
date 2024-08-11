from django.db import models

from apps.common.models import AbstractBaseModel
from apps.wallets.choices import WalletType


class Wallet(AbstractBaseModel):
    public_address = models.CharField(
        verbose_name='Web3 Wallet public address',
        max_length=64
    )
    type = models.CharField(
        verbose_name='Wallet address type',
        max_length=16,
        choices=WalletType,
        default=WalletType.EVM
    )
