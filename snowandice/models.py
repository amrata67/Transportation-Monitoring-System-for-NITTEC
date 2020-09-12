from django.db import models

# Create your models here.
class SnowAndIceLog(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(blank=True, null=True)
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    caller_organization = models.CharField(db_column='Caller Organization', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_phone_field = models.CharField(db_column='Caller Phone #', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    caller_name = models.CharField(db_column='Caller Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cross_street = models.CharField(db_column='Cross Street', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direction = models.CharField(db_column='Direction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    route_street = models.CharField(db_column='Route/ Street', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    municipality = models.CharField(db_column='Municipality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operators = models.CharField(db_column='Operators', max_length=50, blank=True, null=True)  # Field name made lowercase.
    owning_agency = models.CharField(db_column='Owning agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    additional_information = models.TextField(db_column='Additional_information', blank=True, null=True)  # Field name made lowercase.
    modtime = models.DateTimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.
    operatorsresponse = models.TextField(db_column='OperatorsResponse', blank=True, null=True)  # Field name made lowercase.
    dotcallout1 = models.NullBooleanField(db_column='DOTCallout1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dotcallout2 = models.NullBooleanField(db_column='DOTCallout2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countyeriecallout1 = models.NullBooleanField(db_column='CountyErieCallout1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countyeriecallout2 = models.NullBooleanField(db_column='CountyErieCallout2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countyniagaracallout1 = models.NullBooleanField(db_column='CountyNiagaraCallout1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    countyniagaracallout2 = models.NullBooleanField(db_column='CountyNiagaraCallout2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    towncallout1 = models.NullBooleanField(db_column='TownCallout1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    towncallout2 = models.NullBooleanField(db_column='TownCallout2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nysta_tsoccallout = models.NullBooleanField(db_column='NYSTA/TSOCCallout', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'snow_and_ice_log'