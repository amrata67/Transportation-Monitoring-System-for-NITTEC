
from django.conf.urls import url
from . import views

app_name = 'weatherConditions'

urlpatterns = [
    url(r'^$', views.weather, name='weather'),
]