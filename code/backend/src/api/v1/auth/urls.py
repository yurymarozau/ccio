from django.urls import include, re_path

# from api.v1.auth.jwt import urls as jwt_urls
from api.v1.auth.web3 import urls as web3_urls

urlpatterns = [
    # re_path(r'^jwt/', include(jwt_urls.urlpatterns)),
    re_path(r'^web3/', include(web3_urls.urlpatterns)),
]
