from django.shortcuts import render, redirect
from django.http import request
from .models import IncidentLog
from tables.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime

def getContext():
    dmsList = []
    for dms in DmsList.objects.all():
        if dms.affectedtype == "DMS":
            dmsList.append(dms.cctv_dms_names)

    context = {
        'detectionMethodList': [dml.detectionmethod for dml in DetectionMethod.objects.all()],
        'routeStreeList': [rs.route_street for rs in RouteStreet.objects.all()],
        'callerNameList': [cm.caller_name for cm in CallerNamePhoneOrg.objects.all()],
        'directionList': [d.direction for d in Direction.objects.all()],
        'callerPhoneList': [cm.phone_numbers for cm in CallerNamePhoneOrg.objects.all()],
        'CallerNamePhoneOrg': [cm for cm in CallerNamePhoneOrg.objects.all()],
        'crossStreetList' : [cs.cross_street for cs in CrossStreet.objects.all()],
        'callerOrganizationList': [cm.caller_organization for cm in CallerNamePhoneOrg.objects.all()],
        'municipalityList': [m.municipality for m in Municipality.objects.all()],
        'owningAgencyList': [oa.member_agency for oa in OwningAgency.objects.all()],
        'generalEventList': [ge.gen_event for ge in GeneralEvent.objects.all()],
        'operatorList': [op.name for op in Operators.objects.all()],
        'dmsList': dmsList,
        'pvmsList': [pvms.nittec_name_crossroads_description for pvms in PvmsList.objects.all()],
        'helpHowNotifyList' : [h.hownotified for h in HelpHowNotified.objects.all()],
        'helpActionList' : [ha.actiontaken for ha in HelpActionTaken.objects.all()],
        'helpAssistList' : [hal.typeofasssist for hal in HelpAssistType.objects.all()],
    }
    return context

def isEmpty(data):
    if len(list(data)) == 0:
        return True
    return False

# Find report by clicking on link from home page
def getReport(request,url_report_id):
    if request.method=="GET":
        context = getContext()
        context['unlockPage'] = False
        if url_report_id:
            data = IncidentLog.objects.raw("Select * from incident_log where id = {id}".format(id=url_report_id))
            if isEmpty(data):
                error_message = "Report with ID " + url_report_id + " not found."
                messages.error(request, error_message)
            else:
                context['report'] = data[0]
        else:
            messages.error(request, "Report id is missing .")
    else:
        messages.error(request, "Could not find report!")
        context['unlockPage'] = False
    return render(request, 'incident/incident_congestion.html', context)

def checkLogin(request):
    if request.session.has_key('is_authenticated'):
        if request.session['is_authenticated']:
            return True
    return False

def logout_user(request):
    del request.session['username']
    del request.session['password']
    del request.session['is_authenticated']
    return render(request, 'accounts/login.html')

def incidentCongestion(request):
    if not checkLogin(request):
        print('login failed')
        return redirect('/accounts/login')
    context = getContext()
    if request.method == "POST" and request.POST.get('add_report'):
        return addReport(request)

    if request.method == "POST" and request.POST.get('logout'):
        return logout_user(request)
    
    if request.method == "POST":
        report_id = request.POST.get('id')
        if report_id == "":
            messages.error(request, "Report ID cannot be left empty")
            context['unlockPage'] = False
            context['displayHelpLog'] = False
            context['report'] = None
            return render(request, 'incident/incident_congestion.html', context)

    if request.method == "POST" and request.POST.get('save_report'):
        return saveReport(request)
    
    if request.method == "POST" and request.POST.get('find_report'):
        return findReport(request, None)

    if request.method == "POST" and request.POST.get('fast_left'):
        return findFastLeft(request)
    
    if request.method == "POST" and request.POST.get('left'):
        return findLeft(request)
    
    if request.method == "POST" and request.POST.get('right'):
        return findRight(request)

    if request.method == "POST" and request.POST.get('fast_right'):
        return findFastRight(request)
    
    if request.method == "POST" and request.POST.get('update_report'):
        return updateReport(request)

    if request.method == "POST" and request.POST.get('delete_report'):
        return deleteReport(request)
    report = None
    try:
        report = IncidentLog.objects.latest('id')
        context['report'] =  report
    except ObjectDoesNotExist:
        messages.warning(request, "No records exist in the database")
    if report != None:
        try:
            helpLog = AccessHelpLog.objects.get(pk=report.helplogid)
            context['help'] = helpLog
            context['displayHelpLog'] = False
            if helpLog.referringlog != None and helpLog.referringlog != "":
                context['displayHelpLog'] = True
        except ObjectDoesNotExist:
            messages.warning(request, "No help log found for this record")
    return render(request, 'incident/incident_congestion.html', context)

def convertCheckbox(request, field):
    if (request.POST.get(field) == "on"):
        return True
    return False

def convertBlankStringToNone(request, field):
    if request.POST.get(field) == '':
        return None
    return request.POST.get(field)

def saveReport(request):
    context = getContext()
    report_id = request.POST.get('id')
    operator = request.POST.get('operator')
    try:
        report = IncidentLog.objects.get(pk=report_id)
        saveReport = report

        saveReport = IncidentLog(
            id = report.id,
            closed = convertCheckbox(request, 'status'),
            lockedID = report.lockedID,
            operatorsresponse = request.POST.get('operators_response'),
            cross_street = request.POST.get('cross_street'),
            direction = request.POST.get('direction'),
            route_street = request.POST.get('route_street'),
            municipality = request.POST.get('municipality'),
            event_description = request.POST.get('event_description'),
            caller_organization = request.POST.get('caller_organization'),
            caller_phone_field = request.POST.get('caller_phone'),
            caller_name = request.POST.get('caller_name'),
            owning_agency = request.POST.get('owning_agency'),
            detectmethod = request.POST.get('detection_method'),
            gen_event = request.POST.get('general_event_description'),
            operators = request.POST.get('operator'),
            modtime = datetime.now(),
            date = request.POST.get('date'),
            Time = request.POST.get('time'),
            creventid = request.POST.get('cross_roads_id'),
            cars_active = convertCheckbox(request, 'cars_manual'),
            cars_deactive = convertCheckbox( request, 'cars_deleted'),
            fullroadclosure = convertCheckbox(request, 'full_road_closure'),
            num_lanes_blocked = convertBlankStringToNone(request, 'number_lanes'),
            detectiontime = convertBlankStringToNone(request, 'detection_time'),
            verifytime = convertBlankStringToNone(request, 'verification_time'),
            scenearrtime = convertBlankStringToNone(request, 'scene_arrival_time'),
            lanblockcleartime = convertBlankStringToNone(request, 'lane_clearance_time'),
            cleartime = convertBlankStringToNone(request, 'clearance_time'),
            scenedeparttime = convertBlankStringToNone(request, 'scene_depart_time'),
            retnormtime = convertBlankStringToNone(request, 'normal_conditions'),
            tcws = convertCheckbox(request, 'activated_tcws'),
            tcws_deact = convertCheckbox(request,'deactivated_tcws'),
            hicfsent = convertCheckbox(request,'hcif_initial_form'),
            skyway = convertCheckbox(request,'activated_flashers'),
            skyway_deact = convertCheckbox(request,'deactivated_flashers'),
            crdms_act = convertCheckbox(request,'activated_dms'),
            crdms_deact = convertCheckbox(request,'deactivated_dms'),
            crfaxemail_act = convertCheckbox(request,'activated_fax_email'),
            crfaxemail_deact = convertCheckbox(request,'deactivated_fax_email'),
            crweb_act = convertCheckbox(request,'activated_web'),
            crweb_deact = convertCheckbox(request,'deactivated_web'),
            hicffinalsent = convertCheckbox(request,'hcif_final_form'),
            transalert_act = convertCheckbox(request,'issued_nyalert'),
            transalert_deact = convertCheckbox(request,'deleted_nyalert'),
            dmsactivelist = request.POST.getlist('dms_active_list'),
            pvmsactivelist = request.POST.getlist('pvms_active_list'),
            incseverity = request.POST.get('severity_level'),
            secondaryincident = convertCheckbox(request, 'secondary_incident'),
            secondaryincidentlognum = request.POST.get('secondary_incident_number'),
            priority_response = convertCheckbox(request, 'priority_response'),
            helplogid = report.helplogid,
        )
        helpLog = AccessHelpLog.objects.get(pk=saveReport.helplogid)
        saveHelpLog = helpLog
        if convertCheckbox(request, 'help_activate'):
            saveHelpLog = AccessHelpLog (
                id = helpLog.id,
                incidentstarttime = convertBlankStringToNone(request, 'incident_start_time'),
                dispatchtime = convertBlankStringToNone(request, 'dispatch_time'),
                arrivaltime = convertBlankStringToNone(request, 'arrival_time'),
                numvehiclesmoved = convertBlankStringToNone(request, 'num_vehicals_moved'),
                clearlanetime = convertBlankStringToNone(request, 'clear_lane_time'),
                scenedeparturetime = convertBlankStringToNone(request, 'scene_departure_time'),
                assisttype = request.POST.get('help_assist_type'),
                actiontaken = request.POST.get('help_action_taken'),
                firstonscene = convertCheckbox(request, 'first_on_scene'),
                hownotified = request.POST.get('help_how_notified'),
                operators = request.POST.get('help_operator'),
                referringlog = request.POST.get('referring_log'),
                inputdate = request.POST.get('help_date'),
                inputtime = request.POST.get('help_time'),
                referringlogtype = convertCheckbox(request, 'referring_log_type'),
                referringroute = request.POST.get('referring_route'),
                num_lanes_blocked = convertBlankStringToNone(request, 'lanes_blocked_number'),
            )
            context['displayHelpLog'] = True

        if convertCheckbox(request, 'status'):
            saveReport.closedtime = datetime.now()
            if not convertCheckbox(request, 'help_activate'):
                saveHelpLog.delete()
                saveReport.helplogid = None
                context['displayHelpLog'] = False

        if report.lockedID == True and report.operators == operator:
            saveReport.lockedID = 0
            saveReport.save()
            if convertCheckbox(request, 'help_activate'):
                saveHelpLog.save()
                context['displayHelpLog'] = True
            else:
                context['displayHelpLog'] = False
            messages.success(request, "Report has been successfully saved!")
        else:
            messages.error(request, "Report has not been saved. Update the record before saving.")
        report = IncidentLog.objects.get(pk=report_id)
        context['report'] = report
        helpLog = AccessHelpLog.objects.get(pk=report.helplogid)
        context['help'] = helpLog
    except ObjectDoesNotExist:
        messages.error(request, "Could not find report!")
    context['unlockPage'] = False
    return render(request, 'incident/incident_congestion.html', context)

def addReport(request):
    # FIXME operator field should be fixed by authenticated user
    context = getContext()
    newHelpLog = AccessHelpLog()
    newHelpLog.save()
    
    newReport = IncidentLog(
        operators = request.POST.get('operator'),
        lockedID = 1,
        helplogid = newHelpLog.id,
    )
    newReport.save()
    context['report'] = newReport
    context['help'] = newHelpLog
    messages.success(request, "Successfully created a new report.")
    context['unlockPage'] = True
    context['displayHelpLog'] = False
    return render(request, 'incident/incident_congestion.html', context)
    
def findReport(request, customID):
    context = getContext()
    report_id = request.POST.get('id')
    report = None
    if customID != None:
        report_id = customID
    try:
        report = IncidentLog.objects.get(pk=report_id)
        context['report'] = report
        if report.lockedID == 1:
            fmtMsg = "This report is being edited by: " + report.operators + " Please contact them before editing this report."
            messages.warning(request, fmtMsg)
    except ObjectDoesNotExist:
        fmtMsg = "Report with ID " + str(report_id) + "not found."
        messages.error(request, fmtMsg)
    
    try:
        helpLog = AccessHelpLog.objects.get(pk=report.helplogid)
        context['help'] = helpLog
        context['displayHelpLog'] = False
        if helpLog.referringlog != None and helpLog.referringlog != "":
            context['displayHelpLog'] = True
    except ObjectDoesNotExist:
        messages.warning(request, "No help log found for this record")
    context['unlockPage'] = False
    return render(request, 'incident/incident_congestion.html', context)

def findFastLeft(request):
    report_id = int(request.POST.get('id')) - 10
    return findReport(request, report_id)

def findLeft(request):
    report_id = int(request.POST.get('id')) - 1
    return findReport(request, report_id)

def findRight(request):
    report_id = int(request.POST.get('id')) + 1
    return findReport(request, report_id)

def findFastRight(request):
    report_id = int(request.POST.get('id')) + 10
    return findReport(request, report_id)

def updateReport(request):
    context = getContext()
    report_id = request.POST.get('id')
    report = None
    try:
        report = IncidentLog.objects.get(pk=report_id)
        if not report.lockedID:
            report.lockedID = True
            # FIXME: Should get the authenticated user
            report.operators = request.POST.get('operator')
            context['unlockPage'] = True
            report.save()
            messages.success(request, "You have successfully unlocked this report.")
        elif report.lockedID and report.operators == request.POST.get('operator'):
            messages.success(request, "You have already unlocked this page.")
            context['unlockPage'] = True
        else:
            fmtMsg = "Report locked " + report.operators + " is editing this report."
            messages.error(request,fmtMsg)
        context['report'] = report
    except ObjectDoesNotExist:
        msg="Report with ID " + str(report_id) + " does not exist."
        messages.error(request, msg)
    if report != None:
        try:
            helpLog = AccessHelpLog.objects.get(pk=report.helplogid)
            context['help'] = helpLog
            context['displayHelpLog'] = False
            if helpLog.referringlog != None and helpLog.referringlog != "":
                context['displayHelpLog'] = True
        except ObjectDoesNotExist:
            messages.warning(request, "No help log found for this record")
    return render(request, 'incident/incident_congestion.html', context)

def deleteReport(request):
    context = getContext()
    report_id = request.POST.get('id')
    try:
        report = IncidentLog.objects.get(pk=report_id)
        report.delete()

        helpLog = AccessHelpLog.objects.get(pk=report.helplogid)
        helpLog.delete()
        messages.success(request, "You have successfully deleted the report")
        context['report'] = None
        context['help'] = None
        context['displayHelpLog'] = False
        context['unlockPage'] = False
    except ObjectDoesNotExist:
        fmtMsg = "Report with ID " + id + " does not exist."
        messages.error(request, fmtMsg)
    return render(request, 'incident/incident_congestion.html', context)