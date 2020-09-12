from django.db import models

# Create your models here.
class EquipmentLog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    closed = models.NullBooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    affected_equipment_system = models.CharField(db_column='Affected_Equipment_System', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type_of_problem = models.CharField(db_column='Type_of_Problem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipment_name_cctv_dms_names = models.CharField(max_length=50, blank=True, null=True)
    recorder_name = models.CharField(db_column='Recorder_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_time = models.TimeField(db_column='Start_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_time = models.TimeField(db_column='End_Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    status_notification_outside_support_information = models.TextField(db_column='Status_Notification_Outside_Support_Information', blank=True, null=True)  # Field name made lowercase.
    nittec_system_staff_action_taken = models.TextField(db_column='Nittec_System_Staff_Action_Taken', blank=True, null=True)  # Field name made lowercase.
    reporting_name = models.CharField(db_column='Reporting_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reporting_member_agency = models.CharField(db_column='Reporting_Member_Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone_Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticket_number_nysdot_ticker_number = models.CharField(db_column='Ticket_number_NYSDOT_Ticker_Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    outside_support = models.CharField(db_column='Outside_Support', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owning_agency = models.CharField(db_column='Owning_Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    outofservice_needsmaintenance_operational_status = models.IntegerField(db_column='OutOfService_NeedsMaintenance_Operational Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modtime = models.TimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.
    cctvontime = models.TimeField(db_column='CCTVOnTime', blank=True, null=True)  # Field name made lowercase.
    cctvondate = models.DateField(db_column='CCTVOnDate', blank=True, null=True)  # Field name made lowercase.
    cctvofftime = models.TimeField(db_column='CCTVOffTime', blank=True, null=True)  # Field name made lowercase.
    cctvoffdate = models.DateField(db_column='CCTVOffDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'equipment_log'