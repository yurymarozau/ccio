from django.http import JsonResponse
from rest_framework import permissions
from siwe import generate_nonce

from api.base.views import BaseAPIView


class GenerateNonceAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return JsonResponse(dict(nonce=generate_nonce()))
