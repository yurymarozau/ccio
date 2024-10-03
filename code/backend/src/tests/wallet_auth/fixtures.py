import random

import arrow
import pytest
import siwe

from apps.wallets.choices import ChainIDChoices
from apps.wallets.models import Wallet
from tests.common.fixtures import *
from tests.wallet_auth.utils import generate_eip55_address


@pytest.fixture
def domain():
    return '127.0.0.1:8000'


@pytest.fixture
def uri(domain):
    return f"http://{domain}"


@pytest.fixture
def wallet(wallet_model_factory):
    return wallet_model_factory()


@pytest.fixture
def public_address():
    return generate_eip55_address()


@pytest.fixture
def chain_id():
    return random.choice(ChainIDChoices.values)


@pytest.fixture
def nonce():
    return siwe.generate_nonce()


@pytest.fixture
def siwe_message_with_first_auth_wallet(domain, uri, public_address, chain_id, nonce):
    Wallet.objects_all.filter(public_address=public_address).delete()
    issued_at = arrow.utcnow()
    expiration_time = arrow.get(issued_at).shift(hours=4)

    message = siwe.SiweMessage(
        domain=domain,
        uri=uri,
        address=public_address,
        version='1',
        chain_id=chain_id,
        nonce=nonce,
        issued_at=siwe.ISO8601Datetime.from_datetime(issued_at.datetime),
        expiration_time=siwe.ISO8601Datetime.from_datetime(expiration_time.datetime)
    )
    return message
