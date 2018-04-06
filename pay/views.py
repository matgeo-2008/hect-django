from django.shortcuts import render
from .models import Broker


def brokerlist(request):
    all_brokers = Broker.objects.all()
    return render(request, 'pay/brokerlist.html', {'all_brokers': all_brokers})

