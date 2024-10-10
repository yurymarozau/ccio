from pytest_factoryboy import register

from tests.wallet_auth.factories import WalletModelFactory
from tests.wallet_auth.fixtures import *

register(WalletModelFactory, 'wallet_model_instance')
