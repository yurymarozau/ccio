from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from simple_history.models import HistoricalRecords

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


class PortfolioWalletTokenBalance(AbstractBaseModel):
    portfolio_wallet = models.ForeignKey('apps.PortfolioWallet', related_name='token_balances_rel', on_delete=models.CASCADE)
    token = models.ForeignKey('apps.Token', related_name='token_balances_rel', on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=78,
        decimal_places=0,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator((2 ** 256) - 1)],
    )
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = (
            ('portfolio_wallet', 'token'),
        )

    def __str__(self):
        return f"{self.portfolio_wallet} - {self.token} - {self.formatted_balance}"

    @property
    def formatted_balance(self):
        return Decimal(self.balance) / Decimal(10 ** self.token.decimals)
