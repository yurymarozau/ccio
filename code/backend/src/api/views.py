from django.http import JsonResponse
from rest_framework import permissions

from api.base.views import BaseAPIView


class ApiInfoAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        api_info = {
            'current_version': 'v1',
            'supported_versions': ['v1',],
        }
        return JsonResponse(api_info)
