import uuid

import siwe
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from apps.wallets.choices import WalletType
from apps.wallets.models import LoginWallet


class WalletBackend(BaseBackend):
    def authenticate(self, request, message=None, signature=None, **kwargs):
        if not message or not signature:
            return

        try:
            siwe_message = siwe.SiweMessage.from_message(message=message)
            siwe_message.verify(signature=signature)
        except siwe.VerificationError:
            return

        login_wallet = LoginWallet.objects.filter(address=siwe_message.address).first()
        if login_wallet:
            user = User.objects.get(login_wallets_rel=login_wallet)
        else:
            user = User(username=uuid.uuid4().hex)
            user.set_unusable_password()
            user.save()
            LoginWallet.objects.create(
                user=user,
                address=siwe_message.address,
                type=WalletType.EVM
            )
        return user


    def get_user(self, user_id):
        return User.objects.get(pk=user_id)
