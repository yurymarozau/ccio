from django.db import models

from apps.common.models import AbstractBaseModel


class Portfolio(AbstractBaseModel):
    user = models.ForeignKey('apps.User', related_name='portfolios_rel', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({'Active' if self.is_enabled else 'Disabled'})"


class PortfolioWallet(AbstractBaseModel):
    portfolio = models.ForeignKey('apps.Portfolio', related_name='portfolio_wallets_rel', on_delete=models.CASCADE)
    wallet = models.ForeignKey('apps.Wallet', related_name='portfolio_wallets_rel', on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.portfolio} - {self.wallet} - {'Active' if self.is_enabled else 'Disabled'}"
