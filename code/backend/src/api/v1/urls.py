from django.urls import include, re_path

from api.v1 import views
from api.v1.auth import urls as auth_urls
from api.v1.portfolio import urls as portfolio_urls

urlpatterns = [
    re_path(r'^health-check/', views.HealthCheck.as_view()),
    re_path(r'^auth/', include(auth_urls.urlpatterns)),
    re_path(r'^portfolio/', include(portfolio_urls.urlpatterns)),
]
