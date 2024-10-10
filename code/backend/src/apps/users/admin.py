from django.contrib import admin

from apps.users.models import User
from apps.wallets.models import LoginWallet


class LoginWalletInline(admin.TabularInline):
    model = LoginWallet


class UserAdmin(admin.ModelAdmin):
    inlines = [LoginWalletInline]


admin.site.register(User, UserAdmin)
