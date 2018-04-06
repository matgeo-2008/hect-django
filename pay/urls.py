from django.conf.urls import url
from . import views

app_name = 'pay'

urlpatterns = [
    url(r'^brokerlist/$', views.brokerlist, name='brokerlist'),
]