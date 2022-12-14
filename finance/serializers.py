from rest_framework import serializers


class AccessToken(serializers.Serializer):
    access_token = serializers.CharField(max_length=100, required=True)
    item_id = serializers.CharField(max_length=100, required=True)
