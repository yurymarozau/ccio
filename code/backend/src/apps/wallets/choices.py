from django.db import models
from django.utils.translation import gettext_lazy as _


class WalletType(models.TextChoices):
    """
    Determines wallet's address type.
    """
    EVM = 'EVM', _('EVM')
