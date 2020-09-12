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
from GeneralEvents.models import Operators

# Create your models here.

class AmberAlertTable(Model):
    report_id = IntegerField()

    Operator = OneToOneField(Operators, null=True, on_delete=models.SET_NULL)
    status = BooleanField()

    date = DateField()
    time = TimeField()

    NYSTA_SOC = BooleanField()
    NYSTA_SOC_Number = CharField(max_length=10)
    NYSDOT_Region_10 = BooleanField()
    NYSDOT_Region_10_Number = CharField(max_length=10)
    NYS_Extra = BooleanField()

    Operator_Notification_TOC = BooleanField()
    Operator_Notification_NYSTA_Traffic = BooleanField()


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

    



