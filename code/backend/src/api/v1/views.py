from django.db import connections
from django.http import JsonResponse
from rest_framework import permissions, views


class HealthCheck(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        connections['default'].cursor()
        return JsonResponse({})
