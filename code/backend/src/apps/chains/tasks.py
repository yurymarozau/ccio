import requests
from django.db import transaction

from apps.chains.models import Chain, ChainRPC, Token
from apps.common.tasks import BaseTask
from apps.common.utils.sentry_service import SentryService


class UpdateTokensTask(BaseTask):
    def custom_run(self, chain_pk, native_token_json):
        chain = Chain.objects.get(pk=chain_pk)
        gecko_tokens_response = requests.get(f'https://tokens.coingecko.com/{chain.gecko_id}/all.json')
        gecko_tokens_json = gecko_tokens_response.json()['tokens']
        self.process_tokens(chain, gecko_tokens_json, native_token_json)

    @staticmethod
    def update_native_token(chain, native_token_json):
        Token.objects.get_or_create(
            chain=chain,
            address=None,
            defaults=dict(
                is_native=True,
                name=native_token_json['name'],
                symbol=native_token_json['symbol'],
                decimals=native_token_json['decimals'],
            )
        )

    @staticmethod
    def update_token(chain, gecko_token_json):
        Token.objects.update_or_create(
            chain=chain,
            address=gecko_token_json['address'],
            defaults=dict(
                name=gecko_token_json['name'],
                symbol=gecko_token_json['symbol'],
                decimals=gecko_token_json['decimals'],
                logo_uri=gecko_token_json.get('logoURI', None),
            )
        )

    def process_tokens(self, chain, gecko_tokens_json, native_token_json):
        self.update_native_token(chain, native_token_json)
        for gecko_token_json in gecko_tokens_json:
            self.update_token(chain, gecko_token_json)


class UpdateChainsListTask(BaseTask):
    def custom_run(self):
        self.fetch_chains()
        self.send_sentry_finish_message()

    @staticmethod
    def get_gecko_chain_json_by_chain_id(gecko_chains_json, chain_id):
        for gecko_chain_json in gecko_chains_json:
            if gecko_chain_json['chain_identifier'] == chain_id:
                return gecko_chain_json

    @staticmethod
    def update_chain(chain_json, gecko_chain_json):
        chain, _ = Chain.objects.update_or_create(
            chain_id=chain_json['chainId'],
            defaults=dict(
                name=chain_json['name'],
                short_name=chain_json['shortName'],
                network_id=chain_json['networkId'],
                info_url=chain_json['infoURL'],
                gecko_id=gecko_chain_json['id'],
                gecko_logo_thumb_url=gecko_chain_json['image']['thumb'],
                gecko_logo_small_url=gecko_chain_json['image']['small'],
                gecko_logo_large_url=gecko_chain_json['image']['large'],
            )
        )
        return chain

    @staticmethod
    def update_rpcs(rpc_urls, chain):
        for rpc_url in rpc_urls:
            ChainRPC.objects.get_or_create(
                chain=chain,
                url=rpc_url,
            )

    @staticmethod
    def update_tokens(chain, native_token_json):
        UpdateTokensTask().apply_async(
            args=(
                chain.pk,
                native_token_json,
            )
        )


    def process_chain(self, chain_json, gecko_chain_json):
        with transaction.atomic():
            chain = self.update_chain(chain_json, gecko_chain_json)
            self.update_rpcs(chain_json['rpc'], chain)
        self.update_tokens(chain, chain_json['nativeCurrency'])


    def fetch_chains(self):
        chains_response = requests.get('https://chainid.network/chains_mini.json')
        chains_json = chains_response.json()

        gecko_chains_response = requests.get('https://api.coingecko.com/api/v3/asset_platforms')
        gecko_chains_json = gecko_chains_response.json()

        for chain_json in chains_json:
            gecko_chain_json = self.get_gecko_chain_json_by_chain_id(gecko_chains_json, chain_json['chainId'])
            if not gecko_chain_json:
                continue
            self.process_chain(chain_json, gecko_chain_json)

    @staticmethod
    def send_sentry_finish_message():
        SentryService.capture_message(message='Chain update has been completed')
