
from django.conf.urls import url
from . import views

app_name = 'snowAndIceResidency'

urlpatterns = [
    url(r'^$', views.residency, name='residency'),
]