from django.conf.urls import url
from . import views

app_name = 'pvms'

urlpatterns = [
    url(r'^$', views.pvms, name='pvms'),
]