from django.urls import re_path

from api.v1.portfolio import views as portfolio_views

urlpatterns = [
    re_path(r'^$', portfolio_views.PortfolioAPIView.as_view(), name='portfolio'),
]
