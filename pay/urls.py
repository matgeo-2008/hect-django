from django.conf.urls import url, include
from . import views
# from .api import urls

app_name = 'pay'

urlpatterns = [
    url(r'^brokerlist/$', views.brokerlist, name='brokerlist'),
    url(r'^broker/(?P<broker_id>[0-9]+)/$', views.brokerprofile, name='brokerprofile'),

    url(r'^brokerlistapi/$', views.brokerListAPI.as_view(), name='brokerlistapi'),
    # url(r'^api/', include('api.urls')),
]