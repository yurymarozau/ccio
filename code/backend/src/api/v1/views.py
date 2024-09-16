from django.db import connections
from django.http import JsonResponse
from rest_framework import permissions

from api.base.views import BaseAPIView


class HealthCheck(BaseAPIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        connections['default'].cursor()
        return JsonResponse({})
