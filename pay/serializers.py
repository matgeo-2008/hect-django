from rest_framework import serializers
from .models import Broker


class brokerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Broker
        fields = '__all__'
