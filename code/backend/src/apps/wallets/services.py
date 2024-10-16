from decimal import Decimal
from typing import Type

from web3 import Web3

from apps.chains.models import ChainRPC, Token
from apps.common.constants import erc20_abi
from apps.common.services import BaseModelService
from apps.wallets.models import Wallet


class WalletModelService(BaseModelService):
    def __init__(self, wallet: Wallet):
        self._wallet = wallet

    @property
    def model(self) -> Type[Wallet]:
        return Wallet

    @property
    def wallet(self) -> Wallet:
        return self._wallet

    @property
    def balance(self) -> Decimal:
        token = Token.objects.get(
            symbol='ZRO',
            chain__chain_id=42161
        )
        rpc = ChainRPC.objects.filter(chain__chain_id=42161, is_enabled=True).order_by('-weight').first()
        if not rpc:
            return Decimal('0')

        web3 = Web3(Web3.HTTPProvider(rpc.url))

        if web3.is_connected():
            token_address = web3.to_checksum_address(token.address)
            wallet_address = web3.to_checksum_address(self.wallet.public_address)
            token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
            balance = token_contract.functions.balanceOf(wallet_address).call()
            return Decimal(balance) / Decimal(10 ** token.decimals)

        return Decimal('0')
