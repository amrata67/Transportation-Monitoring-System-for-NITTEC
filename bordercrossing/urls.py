
from django.conf.urls import url
from . import views

app_name = 'bordercrossing'

urlpatterns = [
    url(r'^$', views.page, name='page'),
]