from django.db import models

# Create your models here.
class SnowIceResidency(models.Model):
    screennum = models.CharField(db_column='ScreenNum', max_length=50, primary_key=True)  # Field name made lowercase.
    residencynameshort = models.CharField(db_column='ResidencyNameShort', max_length=50, blank=True, null=True)  # Field name made lowercase.
    residencynamefull = models.CharField(db_column='ResidencyNameFull', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    othernumber = models.CharField(db_column='OtherNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    status = models.NullBooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sibordercolor = models.CharField(db_column='SIBorderColor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backgroundactivecolor = models.CharField(db_column='BackgroundActiveColor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    backgroundinactivecolor = models.CharField(db_column='BackGroundInActiveColor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    activetextcolor = models.CharField(db_column='ActiveTextColor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inactivetextcolor = models.CharField(db_column='InActiveTextColor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calloutlvl = models.IntegerField(db_column='CallOutLvl', blank=True, null=True)  # Field name made lowercase.
    activedate = models.DateField(db_column='ActiveDate', blank=True, null=True)  # Field name made lowercase.
    activetime = models.TimeField(db_column='ActiveTime', blank=True, null=True)  # Field name made lowercase.
    inactivedate = models.DateField(db_column='InactiveDate', blank=True, null=True)  # Field name made lowercase.
    inactivetime = models.TimeField(db_column='InactiveTime', blank=True, null=True)  # Field name made lowercase.
    truckout = models.IntegerField(db_column='TruckOut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'snow_ice_residency'
