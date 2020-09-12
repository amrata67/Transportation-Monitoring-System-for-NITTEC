from django.db import models

# Create your models here.
class IncidentLog(models.Model):
    closed = models.NullBooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    closedtime = models.DateTimeField(db_column='ClosedTime', blank=True, null=True)  # Field name made lowercase.
    lockedID = models.NullBooleanField(db_column='lockedID',blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    operatorsresponse = models.TextField(db_column='OperatorsResponse', blank=True, null=True)  # Field name made lowercase.
    cross_street = models.CharField(db_column='Cross_Street', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direction = models.CharField(db_column='Direction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    route_street = models.CharField(db_column='Route_Street', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    municipality = models.CharField(db_column='Municipality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    event_description = models.TextField(db_column='Event_Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_organization = models.CharField(db_column='Caller_Organization', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_phone_field = models.CharField(db_column='Caller_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    caller_name = models.CharField(db_column='Caller_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gen_event = models.CharField(db_column='Gen_Event', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operators = models.CharField(db_column='Operators', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Time = models.TimeField(db_column='time',blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    owning_agency = models.CharField(db_column='Owning_Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    detectiontime = models.DateTimeField(db_column='DetectionTime', blank=True, null=True)  # Field name made lowercase.
    verifytime = models.DateTimeField(db_column='VerifyTime', blank=True, null=True)  # Field name made lowercase.
    scenearrtime = models.DateTimeField(db_column='SceneArrTime', blank=True, null=True)  # Field name made lowercase.
    lanblockcleartime = models.DateTimeField(db_column='LanBlockClearTime', blank=True, null=True)  # Field name made lowercase.
    cleartime = models.DateTimeField(db_column='ClearTime', blank=True, null=True)  # Field name made lowercase.
    scenedeparttime = models.DateTimeField(db_column='SceneDepartTime', blank=True, null=True)  # Field name made lowercase.
    retnormtime = models.DateTimeField(db_column='RetNormTime', blank=True, null=True)  # Field name made lowercase.
    cars_active = models.NullBooleanField(db_column='CARS_active', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    cars_deactive = models.NullBooleanField(db_column='CARS_deactive', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    modtime = models.DateTimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.
    fullroadclosure = models.NullBooleanField(db_column='FullRoadClosure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dmsactivelist = models.TextField(db_column='DMSActiveList', blank=True, null=True)  # Field name made lowercase.
    transalert_act = models.NullBooleanField(db_column='TransAlert_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    transalert_deact = models.NullBooleanField(db_column='TransAlert_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    tcws = models.NullBooleanField(db_column='TCWS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skyway = models.NullBooleanField(db_column='Skyway', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hicfsent = models.NullBooleanField(db_column='HICFSent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    crdms_act = models.NullBooleanField(db_column='CRDMS_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crdms_deact = models.NullBooleanField(db_column='CRDMS_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crfaxemail_act = models.NullBooleanField(db_column='CRFaxEmail_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crfaxemail_deact = models.NullBooleanField(db_column='CRFaxEmail_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crweb_act = models.NullBooleanField(db_column='CRWeb_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crweb_deact = models.NullBooleanField(db_column='CRWeb_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    num_lanes_blocked = models.IntegerField(db_column='Num_Lanes_Blocked', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hicffinalsent = models.NullBooleanField(db_column='HICFFinalSent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondaryincident = models.NullBooleanField(db_column='SecondaryIncident', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondaryincidentlognum = models.CharField(db_column='SecondaryIncidentLogNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    incseverity = models.IntegerField(db_column='IncSeverity', blank=True, null=True)  # Field name made lowercase.
    creventid = models.CharField(db_column='CREventID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    detectmethod = models.CharField(db_column='DetectMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pvmsactivelist = models.TextField(db_column='PVMSActiveList', blank=True, null=True)  # Field name made lowercase.
    skyway_deact = models.NullBooleanField(db_column='Skyway_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    tcws_deact = models.NullBooleanField(db_column='TCWS_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    priority_response = models.NullBooleanField(db_column='Priority_Response', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    helplogid = models.IntegerField(db_column='HelpLogID', blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'incident_log'
