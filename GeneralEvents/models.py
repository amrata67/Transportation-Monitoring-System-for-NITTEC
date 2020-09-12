from django.db import models
from django.db.models import Model
from django.db.models import (
    IntegerField,
    CharField,
    BooleanField,
    TextField,
    DateField,
    TimeField,
    OneToOneField,
)
# Create your models here.

class CallerDetails(Model):
    caller_name = TextField()
    caller_phone = CharField(max_length = 10)
    caller_organisation = TextField()


class Operators(Model):
    name = TextField()

class GeneralEventsTable(Model):
    report_id = IntegerField()

    Operator = OneToOneField(Operators, null=True, on_delete=models.SET_NULL)

    TYPE_CHOICES = (
        ('PSF', 'Public Safety Campaign' ),
        ('SE', 'Special Event'),
    )
    Type = CharField(max_length = 120, choices = TYPE_CHOICES)

    status = BooleanField()

    date = DateField()
    time = TimeField()

    Event_name = TextField()

    caller_details = OneToOneField(CallerDetails, null=True, on_delete=models.SET_NULL)


    start_date = DateField()
    start_time = TimeField()
    end_date = DateField()
    end_time = DateField()

    General_information = TextField()

    Crossroads_ID = IntegerField()
    Crossroads_activated_DMS = BooleanField()
    Crossroads_activated_Fax_Email = BooleanField()
    Crossroads_activated_Web = BooleanField()
    Crossroads_deactivated_DMS = BooleanField()
    Crossroads_deactivated_Fax_Email = BooleanField()
    Crossroads_deactivated_Web = BooleanField()
    Crossroads_Website_entered = BooleanField()
    Crossroads_Website_deactivated = BooleanField()

    DMS_Activation_time = BooleanField()
    DMS_Deactivation_time = BooleanField()

    PVMS_Activation_time = BooleanField()
    PVMS_Deactivation_time = BooleanField()
    
    HAR_Activation_time = BooleanField()
    HAR_Deactivation_time = BooleanField()


