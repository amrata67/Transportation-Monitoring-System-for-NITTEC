from django.http import HttpResponse, request
from django.apps import apps
from django.template import loader
from .models import DamageClaimsLog
from django.shortcuts import redirect, reverse, render
from datetime import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


Operators = apps.get_model('tables', 'Operators')
all_Operators = Operators.objects.all()
context = {
    'all_Operators': all_Operators
}


def addReport(request):
    newReport = DamageClaimsLog(
        operators = request.POST.get('operator_name'),
        lockedID = 1,
    )
    newReport.save()
    context['report'] = newReport
    messages.success(request, "Successfully started a report. Click 'Save Report' to save.")
    context['unlockPage'] = True
    return render(request, 'DamageClaims/index.html', context)

def saveReport(request):
    report_id = request.POST.get('id')
    operator = request.POST.get('operator_name')
    report=None
    try:
        report = DamageClaimsLog.objects.get(pk=report_id)
    except ObjectDoesNotExist:
        fmtMsg = "Report with ID " + report_id + "not found."
        messages.error(request, fmtMsg)
        context['unlockPage'] = False
        return render(request, 'DamageClaims/index.html', context)
    saveReport = report
    id = report.id
    lockedID = report.lockedID
    damageclaims_information = request.POST.get('dci')
    date=request.POST.get('datetext')
    time = request.POST['timetext']
    operators = request.POST['operator_name']
    modtime = datetime.now()
    if damageclaims_information=="1":
        name = request.POST['callername']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zipcode']
        phone_number = request.POST['phonenumber']
        nysdot_claims = request.POST.get('nysdot')
        nysdot_claims = resolve(nysdot_claims)
        erie_county = request.POST.get('erie')
        erie_county=resolve(erie_county)
        nysta = request.POST.get('nysta')
        nysta = resolve(nysta)
        other = request.POST['other']
        vehicle_infomation = request.POST.get('vehicle_info')
        saveReport = DamageClaimsLog(id=id, lockedID=lockedID, date=date, time=time,name=name, address=address, city=city,state=state,zip=zip,phone_number=phone_number,
        nysdot_claims=nysdot_claims, erie_county=erie_county, nysta=nysta, other=other,operators=operators, vehicle_infomation=vehicle_infomation,
        damageclaims_information=damageclaims_information, modtime=modtime)   
    else:
        information_box=request.POST['general_info']  
        saveReport = DamageClaimsLog(id=id, lockedID=lockedID,date=date, time=time,operators=operators,damageclaims_information="2", modtime=modtime,
        information_box =information_box)
    if report.lockedID == True and report.operators == operator:
        saveReport.lockedID = 0
        saveReport.save()
        messages.success(request, "Report has been successfully saved!")
    else:
        messages.error(request, "Report has not been saved. Update the record before saving.")
    context['report'] = saveReport

    context['unlockPage'] = False
    return render(request, 'DamageClaims/index.html', context)


def resolve(variable):
    variable="1" if variable=="1" else "0"
    return variable


def deleteReport(request):
    id = request.POST.get('id')
    try:
        report = DamageClaimsLog.objects.get(pk=id)
        report.delete()
        messages.success(request, "Report has been successfully deleted!")
    except ObjectDoesNotExist:
        fmtMsg = "Report with ID " +id + " does not exist."
        messages.error(request, fmtMsg)
    context['report'] = DamageClaimsLog()
    return render(request, 'DamageClaims/index.html', context)
        


def damageclaimsform(request):
    print(request)
    if request.method == "POST" and request.POST.get('add_report'):
        return addReport(request)

    if request.method == "POST" and request.POST.get('save_report'):
        return saveReport(request)
    
    if request.method == "POST" and request.POST.get('find_report'):
        return findReport(request)
    
    if request.method == "POST" and request.POST.get('update_report'):
        return updateReport(request)

    if request.method == "POST" and request.POST.get('delete_report'):
        return deleteReport(request)
    
    if request.method == "POST" and request.POST.get('left'):
        return getPrevious(request)

    if request.method == "POST" and request.POST.get('right'):
        return getNext(request)

    if request.method == "POST" and request.POST.get('fast_right'):
        return FastNext(request)
    
    if request.method == "POST" and request.POST.get('fast_left'):
        return FastPrevious(request)

    return render(request, 'DamageClaims/index.html', context)


def updateReport(request):
    report_id = request.POST.get('id')
    try:
        report = DamageClaimsLog.objects.get(pk=report_id)
        if not report.lockedID:
            report.lockedID = True
            report.operators = request.POST.get('operator_name')
            context['unlockPage'] = True
            report.save()
            messages.success(request, "You have successfully unlocked this report. Click 'Save Report' to save.")
        elif report.lockedID and report.operators == request.POST.get('operator_name'):
            messages.success(request, "You have already unlocked this page.")
            context['unlockPage'] = True
        else:
            fmtMsg = "Report locked " + report.operators + " is editing this report."
            messages.error(request,fmtMsg)
        context['report'] = report
    except ObjectDoesNotExist:
        msg="Report with ID " +report_id + " does not exist."
        messages.error(request, msg)
    return render(request, 'DamageClaims/index.html', context)


    
def findReport(request):
    report_id = request.POST.get('id')
    try:
        report = DamageClaimsLog.objects.get(pk=report_id)
        context['report'] = report
        if report.lockedID == 1:
            fmtMsg = "This report is being edited by: " + report.operators + " Please contact them before editing this report."
            messages.warning(request, fmtMsg)
    except ObjectDoesNotExist:
        fmtMsg = "Report with ID " + report_id + "not found."
        context['report']= DamageClaimsLog()
        messages.error(request, fmtMsg)
    context['unlockPage'] = False
    return render(request, 'DamageClaims/index.html', context)


def getPrevious(request):
    report_id = request.POST.get('id')
    preSet =DamageClaimsLog.objects.filter(id__lt = report_id)
    if  preSet.count() > 0:
        pre= preSet.order_by('-id')[0].id
        report = DamageClaimsLog.objects.get(pk=pre)

    else:
        messages.error(request, "No more previous record found.")
        report = DamageClaimsLog.objects.get(pk=report_id)
    context['report'] = report
    return render(request, 'DamageClaims/index.html', context)

def getNext(request):
    report_id = request.POST.get('id')
    nextSet =DamageClaimsLog.objects.filter(id__gt = report_id)
    if  nextSet.count() > 0:
        nextItem= nextSet.order_by('id')[0].id
        report = DamageClaimsLog.objects.get(pk=nextItem)

    else:
        messages.error(request, "No more next record found.")
        report = DamageClaimsLog.objects.get(pk=report_id)
    context['report'] = report
    return render(request, 'DamageClaims/index.html', context)

def FastNext(request):
    report_id = request.POST.get('id')
    nextSet =DamageClaimsLog.objects.filter(id__gt = report_id)
    if  nextSet.count() == 0:
        messages.error(request, "No more next record found.")
        report = DamageClaimsLog.objects.get(pk=report_id)
    elif nextSet.count() < 5:
        LastItem= nextSet.order_by('-id')[0].id
        report = DamageClaimsLog.objects.get(pk=LastItem)
    else:
        fastnext=DamageClaimsLog.objects.raw('select * from damage_claims_log where id in (select id from damage_claims_log where id > %s) ORDER BY id LIMIT 1 OFFSET 4;',[report_id])[0].id
        report = DamageClaimsLog.objects.get(pk=fastnext)
    context['report'] = report

    return render(request, 'DamageClaims/index.html', context)

def FastPrevious(request):
    report_id = request.POST.get('id')
    preSet =DamageClaimsLog.objects.filter(id__lt = report_id)
    if  preSet.count() == 0:
        messages.error(request, "No more previous record found.")
        report = DamageClaimsLog.objects.get(pk=report_id)
    elif preSet.count() < 5:
        firstItem= preSet.order_by('id')[0].id
        report = DamageClaimsLog.objects.get(pk=firstItem)
    else:
        fastpre=DamageClaimsLog.objects.raw('select * from damage_claims_log where id in (select id from damage_claims_log where id < %s) ORDER BY -id LIMIT 1 OFFSET 4;',[report_id])[0].id
        report = DamageClaimsLog.objects.get(pk=fastpre)
    context['report'] = report

    return render(request, 'DamageClaims/index.html', context)