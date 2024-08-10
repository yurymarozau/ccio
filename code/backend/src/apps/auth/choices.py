from django.db import models
from django.utils.translation import gettext_lazy as _


class WalletType(models.TextChoices):
    """
    Determines is wallet's address EVM compatible or not.
    """
    EVM = 'OP', _('Open')
    NON_EVM = 'CL', _('Closed')
