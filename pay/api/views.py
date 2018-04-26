from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pay.models import Broker, Owner, Tenant
from .serializers import BrokerSerializer, TenantSerializer
from .permissions import IsOwnerOrReadOnly


class BrokerAPIView(APIView):

    def get(self, request):
        query = self.request.GET.get("q")
        broker = get_object_or_404(Broker, pk=query)
        serializer = BrokerSerializer(broker, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
