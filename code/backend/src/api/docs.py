from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

schema_view = get_schema_view(
    openapi.Info(
        title='CCIO - Crypto Chart IO',
        default_version='v1',
    ),
    public=True,
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
]
