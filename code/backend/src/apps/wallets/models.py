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

    class Meta:
        indexes = [
            models.Index(fields=['public_address']),
        ]

    def __str__(self):
        return f"{self.public_address} ({self.type})"


class LoginWallet(AbstractBaseModel):
    user = models.ForeignKey('apps.User', related_name='login_wallets_rel', on_delete=models.CASCADE)
    wallet = models.OneToOneField('apps.Wallet', related_name='login_wallet_rel', on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'wallet']),
        ]

    def __str__(self):
        return f"{self.user} - {self.wallet})"
