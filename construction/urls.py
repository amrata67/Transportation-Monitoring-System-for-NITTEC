from django.conf.urls import url
from . import views

app_name = 'construction'

urlpatterns = [
    url(r'^$', views.constructionMaintenance, name='constructionMaintenance'),
    url(r'^projects', views.projects, name='projects'),
    url(r'^add_project', views.addProject, name='addProject'),
]