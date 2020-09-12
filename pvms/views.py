from django.shortcuts import render
from django.http import request

def pvms(request):
    return render(request, 'pvms/pvms.html')
