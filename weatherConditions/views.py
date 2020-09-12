from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def weather(request):

    # projectsList = Project.objects.all()
    # context = {
    #     'projectList': projectsList,
    # }
    return render(request, 'weatherConditions/weather.html');
