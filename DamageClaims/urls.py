from django.conf.urls import url
from . import views

app_name = 'DamageClaims'

urlpatterns = [
    url(r'^$',views.damageclaimsform ,name='damageclaimsform'),
]
