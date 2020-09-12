from django.db import models

# Create your models here.

class DamageClaimsLog(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time',blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='zip', max_length=50, blank=True, null=True)
    phone_number = models.CharField(db_column='Phone_Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nysdot_claims = models.NullBooleanField(db_column='NYSDOT_Claims', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    erie_county = models.NullBooleanField(db_column='Erie_County', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    nysta = models.NullBooleanField(db_column='NYSTA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    other = models.CharField(db_column='Other', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operators = models.CharField(db_column='Operators', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_infomation = models.TextField(db_column='vehicle_infomation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    information_box = models.TextField(db_column='Information_box', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    damageclaims_information = models.IntegerField(db_column='DamageClaims_Information', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lockedID = models.NullBooleanField(db_column='lockedID',blank=True, null=True)
    modtime = models.DateTimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.

    
    class Meta:
        managed = True
        db_table = 'damage_claims_log'


