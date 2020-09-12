from django.db import models

# Create your models here.
class Bordercrossinglog(models.Model):
    closed = models.NullBooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    closedtime = models.DateTimeField(db_column='ClosedTime', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    comments_event_description = models.TextField(db_column='Comments_Event_Description', blank=True, null=True)  # Field name made lowercase.
    owning_agency = models.CharField(db_column='Owning Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_organization = models.CharField(db_column='Caller_Organization', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_phone_field = models.CharField(db_column='Caller_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    caller_name = models.CharField(db_column='Caller_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operators = models.CharField(db_column='Operators', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    modtime = models.DateTimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.
    detectiontime = models.TimeField(db_column='DetectionTime', blank=True, null=True)  # Field name made lowercase.
    retnormtime = models.TimeField(db_column='RetNormTime', blank=True, null=True)  # Field name made lowercase.
    dms = models.NullBooleanField(db_column='DMS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dms_act_time = models.TimeField(db_column='DMS_Act_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dms_deact_time = models.TimeField(db_column='DMS_DeAct_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pvms = models.NullBooleanField(db_column='PVMS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pvms_act_time = models.TimeField(db_column='PVMS_Act_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pvms_deact_time = models.TimeField(db_column='PVMS_DeAct_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har = models.NullBooleanField(db_column='HAR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    har_act_time = models.TimeField(db_column='HAR_Act_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har_act_notifytsoc = models.TimeField(db_column='HAR_Act_NotifyTSOC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har_deact_time = models.TimeField(db_column='HAR_DeAct_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har_deact_notify_tsoc = models.TimeField(db_column='HAR_DeAct_Notify_TSOC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har_update_notify_tsoc = models.TimeField(db_column='HAR_Update_Notify_TSOC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    har_update_activation = models.TimeField(db_column='HAR_Update_Activation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cars_active = models.NullBooleanField(db_column='CARS_active', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    cars_deactive = models.NullBooleanField(db_column='CARS_deactive', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dmsactivelist = models.TextField(db_column='DMSActiveList', blank=True, null=True)  # Field name made lowercase.
    transalert_act = models.NullBooleanField(db_column='TransAlert_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    transalert_deact = models.NullBooleanField(db_column='TransAlert_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    harslot = models.IntegerField(db_column='HARSlot', blank=True, null=True)  # Field name made lowercase.
    pbrtoc = models.IntegerField(db_column='PBrToC', blank=True, null=True)  # Field name made lowercase.
    pbrtou = models.IntegerField(db_column='PBrToU', blank=True, null=True)  # Field name made lowercase.
    rbrtoc = models.IntegerField(db_column='RBrToC', blank=True, null=True)  # Field name made lowercase.
    rbrtou = models.IntegerField(db_column='RBrToU', blank=True, null=True)  # Field name made lowercase.
    lqbrtoc = models.IntegerField(db_column='LQBrToC', blank=True, null=True)  # Field name made lowercase.
    lqbrtou = models.IntegerField(db_column='LQBrToU', blank=True, null=True)  # Field name made lowercase.
    mto_notified_active = models.NullBooleanField(db_column='MTO_Notified_Active', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    mto_notified_cleared = models.NullBooleanField(db_column='MTO_Notified_Cleared', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crdms_act = models.NullBooleanField(db_column='CRDMS_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crdms_deact = models.NullBooleanField(db_column='CRDMS_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crfaxemail_act = models.NullBooleanField(db_column='CRFaxEmail_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crfaxemail_deact = models.NullBooleanField(db_column='CRFaxEmail_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crweb_act = models.NullBooleanField(db_column='CRWeb_Act', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crweb_deact = models.NullBooleanField(db_column='CRWeb_DeAct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    crossroads_creventid = models.CharField(db_column='Crossroads_CREventID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    detectmethod = models.CharField(db_column='DetectMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'border_crossing_log'
