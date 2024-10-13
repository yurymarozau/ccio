from decimal import Decimal
from typing import Type

from apps.common.services import BaseModelService
from apps.wallets.models import Wallet


class WalletModelService(BaseModelService):
    @property
    def model(self) -> Type[Wallet]:
        return Wallet

    @property
    def balance(self) -> Decimal:
        return Decimal('0')
