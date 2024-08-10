from django.urls import include, path

from api.v1 import auth as auth_urls, views

app_name = 'v1'

urlpatterns = [
    path('health-check/', views.HealthCheck.as_view()),
    path('auth/', include(auth_urls.urlpatterns)),
]
