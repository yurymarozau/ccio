import json

from django.contrib.auth import authenticate
from django.urls import reverse

from api.v1.auth.web3.siwe import views
from apps.wallets.models import LoginWallet, Wallet
from tests.common.tests import BaseTestCase


class TestWalletAuth(BaseTestCase):
    def test_get_nonce(self, request_factory):
        request = request_factory.get(reverse('auth-web3-siwe-nonce'))
        response = views.GenerateNonceAPIView.as_view()(request)
        assert response.status_code == 200

        json_response = json.loads(response.content)

        assert json_response.get('nonce')
        assert type(json_response.get('nonce')) is str
        assert len(json_response.get('nonce')) == 11

    def test_wallet_auth_backend(self, request_factory, siwe_message_with_first_auth_wallet):
        """
        Test case with wallet address that has never been authenticated.
        """
        assert siwe_message_with_first_auth_wallet.address
        assert siwe_message_with_first_auth_wallet.chain_id
        assert siwe_message_with_first_auth_wallet.expiration_time

        request = request_factory.get(reverse('auth-web3-siwe-verify'))

        authenticated_user = authenticate(
            request=request,
            message=siwe_message_with_first_auth_wallet.prepare_message(),
            signature='signature',
            mock=True
        )

        authenticated_wallet = Wallet.objects.filter(public_address=siwe_message_with_first_auth_wallet.address).first()
        assert authenticated_wallet

        authenticated_login_wallet = LoginWallet.objects.filter(wallet=authenticated_wallet).first()
        assert authenticated_login_wallet

        assert authenticated_user.is_authenticated
        assert authenticated_user.pk == authenticated_login_wallet.user.pk

    def test_wallet_multiple_auth_backend(self, request_factory, siwe_message_with_first_auth_wallet):
        """
        Test case with multiple authentications of 1 wallet.
        """
        request = request_factory.get(reverse('auth-web3-siwe-verify'))

        authenticate(
            request=request,
            message=siwe_message_with_first_auth_wallet.prepare_message(),
            signature='signature',
            mock=True
        )

        existing_wallet = Wallet.objects.filter(public_address=siwe_message_with_first_auth_wallet.address).first()
        existing_login_wallet = LoginWallet.objects.filter(wallet=existing_wallet).first()
        existing_login_wallet_user = existing_login_wallet.user

        authenticated_user = authenticate(
            request=request,
            message=siwe_message_with_first_auth_wallet.prepare_message(),
            signature='signature',
            mock=True
        )

        authenticated_wallet = Wallet.objects.filter(public_address=siwe_message_with_first_auth_wallet.address).first()
        assert authenticated_wallet

        authenticated_login_wallet = LoginWallet.objects.filter(wallet=authenticated_wallet).first()
        assert authenticated_login_wallet

        assert existing_wallet.pk == authenticated_wallet.pk
        assert existing_login_wallet.pk == authenticated_login_wallet.pk
        assert existing_login_wallet_user.pk == authenticated_user.pk

        assert authenticated_user.is_authenticated
        assert authenticated_user.pk == authenticated_login_wallet.user.pk
