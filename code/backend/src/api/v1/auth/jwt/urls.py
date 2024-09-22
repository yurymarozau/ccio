from django.urls import re_path
from rest_framework_simplejwt import views as drf_jwt_views

urlpatterns = [
    re_path(r'^create/?', drf_jwt_views.TokenObtainPairView.as_view(), name='jwt-create'),
    re_path(r'^refresh/?', drf_jwt_views.TokenRefreshView.as_view(), name='jwt-refresh'),
    re_path(r'^verify/?', drf_jwt_views.TokenVerifyView.as_view(), name='jwt-verify'),
]
