from rest_framework import serializers

from apps.portfolio.models import Portfolio, PortfolioWallet
from apps.wallets.models import Wallet
from apps.wallets.services import WalletModelService


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField(method_name='get_balance')
    class Meta:
        model = Wallet
        fields = ('pk', 'public_address', 'type', 'balance',)
        read_only_fields = ('pk', 'type', 'balance',)

    def get_balance(self, wallet):
        return WalletModelService(wallet).balance


class PortfolioWalletSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()

    class Meta:
        model = PortfolioWallet
        fields = ('wallet', 'is_enabled',)


class PortfolioSerializer(serializers.ModelSerializer):
    portfolio_wallets = PortfolioWalletSerializer(source='portfolio_wallets_rel', many=True)

    class Meta:
        model = Portfolio
        fields = ('pk', 'name', 'is_enabled', 'portfolio_wallets',)
        read_only_fields = ('pk',)
