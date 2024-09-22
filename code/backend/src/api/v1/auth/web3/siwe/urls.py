from django.urls import re_path

from api.v1.auth.web3.siwe import views as siwe_views

urlpatterns = [
    re_path(r'^nonce/$', siwe_views.GenerateNonceAPIView.as_view(), name='auth-web3-siwe-nonce'),

]
