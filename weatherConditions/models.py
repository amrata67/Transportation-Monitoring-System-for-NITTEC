from django.db import models

# Create your models here.
class WeatherRoadConditionsLogs(models.Model):
    general_description = models.TextField(db_column='General_Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reporting_agency = models.CharField(db_column='Reporting_Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operator_response = models.CharField(db_column='Operator_Response', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operators = models.CharField(db_column='Operators', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    modtime = models.DateTimeField(db_column='ModTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'weather_road_conditions_logs'