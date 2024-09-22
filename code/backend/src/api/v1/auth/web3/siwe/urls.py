from django.urls import re_path

from api.v1.auth.web3.siwe import views as siwe_views

urlpatterns = [
    re_path(r'^nonce/$', siwe_views.GenerateNonceAPIView.as_view(), name='auth-web3-siwe-nonce'),
    re_path(r'^verify/$', siwe_views.VerifySiweMessageAPIView.as_view(), name='auth-web3-siwe-verify'),
    re_path(r'^session/$', siwe_views.SiweSessionAPIView.as_view(), name='auth-web3-siwe-session'),
    re_path(r'^signout/$', siwe_views.SiweSignOutAPIView.as_view(), name='auth-web3-siwe-signout'),
]
