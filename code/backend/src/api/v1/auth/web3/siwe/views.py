import arrow
import siwe
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed

from api.base.views import BaseAPIView
from api.v1.auth.web3.siwe.serializers import (SiweMessageSerializer,
                                               SiweSessionSerializer)


class GenerateNonceAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return JsonResponse(dict(nonce=siwe.generate_nonce()))


class VerifySiweMessageAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SiweMessageSerializer

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request=request,
            message=self.validated_data['message'],
            signature=self.validated_data['signature']
        )

        if not user:
            raise AuthenticationFailed()

        login(request, user)

        siwe_message = siwe.SiweMessage.from_message(message=self.validated_data['message'])
        request.session['siwe'] = dict(
            address=siwe_message.address,
            chain_id=siwe_message.chain_id,
        )
        request.session.set_expiry(arrow.get(siwe_message.expiration_time).datetime)
        request.session.save()

        return JsonResponse(dict(verify=True))


class SiweSessionAPIView(BaseAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SiweSessionSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.session.get('siwe', {}))
        return JsonResponse(serializer.initial_data)


class SiweSignOutAPIView(BaseAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse(data={})
