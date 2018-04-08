from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Broker
from .serializers import brokerSerializers


def brokerlist(request):
    all_brokers = Broker.objects.all()
    return render(request, 'pay/brokerlist.html', {'all_brokers': all_brokers})

def brokerprofile(request, broker_id):
    broker = get_object_or_404(Broker, pk=broker_id)
    return render(request, 'pay/broker_profile.html', {'broker': broker})

class brokerListAPI(APIView):

    def get(self, request):
        broker1 = Broker.objects.all()
        serializer = brokerSerializers(broker1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
