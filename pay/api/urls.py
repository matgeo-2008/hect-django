from django.conf.urls import url
from .views import BrokerAPIView

app_name = 'pay'

urlpatterns = [
    url(r'^broker/', BrokerAPIView.as_view(), name='broker-detail'),
]