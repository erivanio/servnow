from rest_framework import serializers
from apps.core.models import Client, Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name')

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    service = ServiceSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'phone', 'service', 'latitude', 'longitude')