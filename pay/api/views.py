from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from pay.models import Broker, Owner, Tenant
from .serializers import BrokerSerializer
from .permissions import IsOwnerOrReadOnly


class BrokerAPIView(APIView):

    def get(self, request):
        query = self.request.GET.get("q")
        broker = get_object_or_404(Broker, pk=query)
        serializer = BrokerSerializer(broker, many=False)
        return Response(serializer.data)
