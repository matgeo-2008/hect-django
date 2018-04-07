from django.shortcuts import render, get_object_or_404
from .models import Broker


def brokerlist(request):
    all_brokers = Broker.objects.all()
    return render(request, 'pay/brokerlist.html', {'all_brokers': all_brokers})

def brokerprofile(request, broker_id):
    broker = get_object_or_404(Broker, pk=broker_id)
    return render(request, 'pay/broker_profile.html', {'broker': broker})
