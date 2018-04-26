from django.conf.urls import url, include
from .views import BrokerAPIView
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'pay'

urlpatterns = [
    url(r'^broker/', BrokerAPIView.as_view(), name='broker-detail'),
    url(r'^token/$', TokenObtainPairView.as_view()),
    url(r'^token/refresh/$', TokenRefreshView.as_view()),
]