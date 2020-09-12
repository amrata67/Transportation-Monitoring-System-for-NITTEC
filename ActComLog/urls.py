from django.conf.urls import url

from . import views

app_name = 'ActComLog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_data/', views.submit_data, name ='submit_data'),
]