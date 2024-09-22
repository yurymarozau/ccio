from django.urls import include, re_path

from api.v1.auth.web3.siwe import urls as siwe_urls

urlpatterns = [
    re_path(r'^siwe/', include(siwe_urls.urlpatterns)),
]
