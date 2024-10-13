from django.contrib import admin

from apps.chains.models import Chain, ChainRPC, Token

admin.site.register(Chain)
admin.site.register(ChainRPC)
admin.site.register(Token)
