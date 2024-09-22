from django.urls import include, re_path

from api.v1 import views
from api.v1.auth import urls as auth_urls

app_name = 'v1'

urlpatterns = [
    re_path(r'^health-check/', views.HealthCheck.as_view()),
    re_path(r'^auth/', include(auth_urls.urlpatterns)),
]
