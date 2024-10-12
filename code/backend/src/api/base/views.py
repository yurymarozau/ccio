from django.utils.functional import cached_property
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from api.base.serializers import BaseSerializer


class BaseAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BaseSerializer

    @cached_property
    def validated_data(self):
        return self.get_validated_data()

    def get_validated_data(self, instance=None):
        serializer = self.get_serializer(instance=instance, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
