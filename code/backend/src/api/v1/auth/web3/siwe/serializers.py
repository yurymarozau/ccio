from rest_framework import serializers

from api.base.serializers import BaseSerializer


class SiweMessageSerializer(BaseSerializer):
    message = serializers.CharField(write_only=True)
    signature = serializers.CharField(write_only=True)


class SiweSessionSerializer(BaseSerializer):
    address = serializers.CharField(read_only=True)
    chain_id = serializers.CharField(read_only=True)
