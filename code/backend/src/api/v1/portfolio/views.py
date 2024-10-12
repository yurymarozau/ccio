from django.http import JsonResponse
from rest_framework import permissions

from api.base.views import BaseAPIView
from api.v1.portfolio.serializers import PortfolioSerializer
from apps.portfolio.models import Portfolio


class PortfolioAPIView(BaseAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
