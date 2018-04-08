from django.conf.urls import url
from . import views

app_name = 'pay'

urlpatterns = [
    url(r'^brokerlist/$', views.brokerlist, name='brokerlist'),
    url(r'^broker/(?P<broker_id>[0-9]+)/$', views.brokerprofile, name='brokerprofile'),

    url(r'^brokerlistapi/$', views.brokerListAPI.as_view(), name='brokerlistapi')
]