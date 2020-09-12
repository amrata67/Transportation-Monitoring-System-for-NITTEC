from django.shortcuts import render
from django.http import request

def debrisLanding(request):
    return render(request, 'debris/debris_signal.html')