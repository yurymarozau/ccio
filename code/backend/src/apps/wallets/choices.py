from django.db import models
from django.utils.translation import gettext_lazy as _


class WalletType(models.TextChoices):
    """
    Determines wallet's address type.
    """
    EVM = 'EVM', _('EVM')


class ChainIDChoices(models.IntegerChoices):
    SEPOLIA = 11155111
    BASE_SEPOLIA = 84532
    LINEA_SEPOLIA = 59141
    ARBITRUM_SEPOLIA = 421614
