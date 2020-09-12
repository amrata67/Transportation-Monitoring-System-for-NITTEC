from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import CommunicationLog

def index(request):
    all_acl = CommunicationLog.objects.all()
    print(all_acl)
    return render(request, 'ActComLog/index.html', {'all_acl':all_acl})

def submit_data(request):
    if request.method=="POST":
        daytoday = request.POST['day_message']
        longtermmessage = request.POST['long_message']
        datestoremember = request.POST['dates_to_remember']
        acl = CommunicationLog(daytoday=daytoday, longtermmessage=longtermmessage, datestoremember=datestoremember)
        acl.save()        
    return redirect(reverse('ActComLog:index'))