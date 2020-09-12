from django.conf.urls import url
from . import views

app_name = 'debris'

urlpatterns = [
    url(r'^$', views.debrisLanding, name='debris'),
]