import uuid

import siwe
from django.contrib.auth.backends import BaseBackend

from apps.users.models import User
from apps.wallets.choices import WalletType
from apps.wallets.models import LoginWallet, Wallet


class WalletBackend(BaseBackend):
    def authenticate(self, request, message=None, signature=None, mock=False, **kwargs):
        if not message or not signature:
            return

        try:
            siwe_message = siwe.SiweMessage.from_message(message=message)
            if not mock:
                siwe_message.verify(signature=signature)
        except siwe.VerificationError:
            return

        wallet, _ = Wallet.objects.get_or_create(
            public_address=siwe_message.address,
            type=WalletType.EVM
        )
        login_wallet = LoginWallet.objects.filter(wallet=wallet).first()
        if login_wallet:
            user = User.objects.get(login_wallets_rel=login_wallet)
        else:
            user = User(username=uuid.uuid4().hex)
            user.set_unusable_password()
            user.save()
            LoginWallet.objects.create(
                user=user,
                wallet=wallet
            )
        return user

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)
