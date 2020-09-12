from django.conf.urls import url
from . import views

app_name = 'incident'

urlpatterns = [
    url(r'^$', views.incidentCongestion, name='incident_congestion'),
    url(r'^getReport/(?P<url_report_id>\d+)/',views.getReport ,name='getReport'),
]