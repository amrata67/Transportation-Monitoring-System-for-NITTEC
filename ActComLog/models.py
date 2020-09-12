from django.db import models

# Create your models here.
class CommunicationLog(models.Model):
    daytoday = models.CharField(db_column='DayToDay', primary_key=True, max_length=200)  # Field name made lowercase.
    longtermmessage = models.TextField(db_column='LongTermMessage', blank=True, null=True)  # Field name made lowercase.
    datestoremember = models.TextField(db_column='DatesToRemember', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'communication_log'