from django.db import models

from apps.common.models import AbstractBaseModel
from apps.wallets.choices import WalletType


class BaseWallet(AbstractBaseModel):
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

    class Meta:
        abstract = True


class LoginWallet(BaseWallet):
    user = models.ForeignKey('apps.User', related_name='login_wallets_rel', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['public_address']),
            models.Index(fields=['user', 'public_address']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['public_address'], name='unique_public_address')
        ]


class Wallet(BaseWallet):
    pass
