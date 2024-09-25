import arrow
import siwe
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated

from api.base.views import BaseAPIView
from api.v1.auth.web3.siwe.serializers import SiweMessageSerializer, SiweSessionSerializer


class GenerateNonceAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return JsonResponse(dict(nonce=siwe.generate_nonce()))


class VerifySiweMessageAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SiweMessageSerializer

    def post(self, request, *args, **kwargs):
        try:
            siwe_message = siwe.SiweMessage.from_message(message=self.validated_data['message'])
            siwe_message.verify(signature=self.validated_data['signature'])
            request.session['siwe'] = dict(
                address=siwe_message.address,
                chain_id=siwe_message.chain_id,
            )
            request.session.set_expiry(arrow.get(siwe_message.expiration_time).datetime)
            request.session.save()
        except:
            raise AuthenticationFailed()
        return JsonResponse(dict(verify=True))


class SiweSessionAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SiweSessionSerializer

    def get(self, request, *args, **kwargs):
        siwe = request.session.get('siwe')
        if not siwe:
            raise NotAuthenticated()
        serializer = self.get_serializer(data=siwe)
        return JsonResponse(serializer.initial_data)


class SiweSignOutAPIView(BaseAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        request.session.flush()
        return JsonResponse(data={})
