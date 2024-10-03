from django.contrib import admin

from apps.wallets.models import LoginWallet, Wallet

admin.site.register(LoginWallet)
admin.site.register(Wallet)
