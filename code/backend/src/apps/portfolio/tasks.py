from decimal import Decimal

import arrow
from django.db.models import F
from web3 import Web3
from web3.exceptions import BadFunctionCallOutput

from apps.chains.models import Chain
from apps.common.constants import erc20_abi
from apps.common.tasks import BaseTask
from apps.common.utils.sentry_service import SentryService
from apps.portfolio.models import Portfolio, PortfolioWalletTokenBalance


class UpdatePortfolioWalletTokensBalance(BaseTask):
    def custom_run(self, *args, **kwargs):
        chains = Chain.objects.prefetch_related('rpcs_rel', 'tokens_rel')
        portfolios = Portfolio.objects.prefetch_related(
            'portfolio_wallets_rel',
        )
        for chain in chains:
            rpc_urls = chain.rpcs_rel.values_list('url', flat=True)
            for rpc_url in rpc_urls:
                try:
                    web3 = Web3(Web3.HTTPProvider(rpc_url))
                    if web3.is_connected():
                        for portfolio in portfolios:
                            for portfolio_wallet in portfolio.portfolio_wallets_rel.all():
                                wallet_address = web3.to_checksum_address(portfolio_wallet.wallet.public_address)
                                tokens = chain.tokens_rel.order_by(
                                    F('token_balances_rel__updated_at').asc(nulls_first=True)
                                ).distinct()
                                for token in tokens:
                                    try:
                                        if token.is_native:
                                            balance = web3.eth.get_balance(wallet_address)
                                        else:
                                            token_address = web3.to_checksum_address(token.address)
                                            token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
                                            balance = token_contract.functions.balanceOf(wallet_address).call()
                                        PortfolioWalletTokenBalance.objects.update_or_create(
                                            portfolio_wallet=portfolio_wallet,
                                            token=token,
                                            defaults=dict(
                                                balance=Decimal(balance),
                                                updated_at=arrow.utcnow().datetime,
                                            )
                                        )
                                    except BadFunctionCallOutput as exc:
                                        SentryService.capture_exception(exc)
                                        continue
                        break
                    else:
                        continue
                except Exception as exc:
                    SentryService.capture_exception(exc)
                    continue
