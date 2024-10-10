import factory

from apps.wallets.models import Wallet
from tests.wallet_auth.utils import generate_eip55_address


class WalletModelFactory(factory.django.DjangoModelFactory):
    public_address = factory.LazyAttribute(lambda obj: generate_eip55_address())

    class Meta:
        model = Wallet
