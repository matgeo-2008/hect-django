from rest_framework import serializers
from pay.models import Broker, Owner, Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class BrokerSerializer(serializers.ModelSerializer):
    tenants = TenantSerializer(many=True, read_only=True)
    owners = OwnerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Broker
        # fields = '__all__'
        fields = [
           'id',
           'email',
           'name',
           'pan_num',
           'bank_acc_num',
           'ifsc',
           'owners',
           'tenants',
        ]
