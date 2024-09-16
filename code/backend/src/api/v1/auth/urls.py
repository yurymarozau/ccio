from django.urls import re_path
from rest_framework_simplejwt import views as drf_jwt_views

from api.v1.auth import views as auth_views

urlpatterns = [
    # JWT
    re_path(r'^jwt/create/?', drf_jwt_views.TokenObtainPairView.as_view(), name='jwt-create'),
    re_path(r'^jwt/refresh/?', drf_jwt_views.TokenRefreshView.as_view(), name='jwt-refresh'),
    re_path(r'^jwt/verify/?', drf_jwt_views.TokenVerifyView.as_view(), name='jwt-verify'),

    # Web3 SIWE
    re_path(r'^web3/nonce/$', auth_views.GenerateNonceAPIView.as_view(), name='web3-nonce'),
]
