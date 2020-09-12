from django.db import models

# Create your models here.
class Operators(models.Model):
    name=models.CharField(primary_key=True, max_length=50)
    username=models.CharField(db_column='username', max_length=20, blank=False, null=False, default='nittec')
    password=models.CharField(db_column='password', max_length=10, blank=False, null=False,  default='nittec')
    admin= models.BooleanField(db_column='admin',default=0)

    class Meta:
        db_table='Operators' 

class BusRoute(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bus_route = models.CharField(db_column='Bus_Route', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'bus_route'


class CallerNamePhoneOrg(models.Model):
    id = models.FloatField(db_column='ID', primary_key=True)  # Field name made lowercase.
    caller_name = models.CharField(db_column='Caller_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone_numbers = models.CharField(db_column='Phone_Numbers', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    caller_organization = models.CharField(db_column='Caller_Organization', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    f5 = models.CharField(db_column='F5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'caller_name_phone_org'


class ConstructionGeneralEvent(models.Model):
    id = models.FloatField(db_column='ID', primary_key=True)  # Field name made lowercase.
    construction_type = models.CharField(db_column='Construction_Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'construction_general_event'


class ConstructionZoneAction(models.Model):
    id = models.IntegerField(primary_key=True)
    action = models.CharField(db_column='Action', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'construction_zone_action'


class CrossStreet(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cross_street = models.CharField(db_column='Cross_Street', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'cross_street'



class Debris(models.Model):
    id = models.IntegerField(primary_key=True)
    debris = models.CharField(db_column='Debris', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'debris'



class DetectionMethod(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    detectionmethod = models.CharField(db_column='DetectionMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'detection_method'


class Direction(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'direction'


class DmsList(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cctv_dms_names = models.CharField(db_column='cctv_dms_names', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    affectedtype = models.CharField(db_column='AffectedType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    affectedtypeindex = models.IntegerField(db_column='AffectedTypeIndex', blank=True, null=True)  # Field name made lowercase.
    owningag = models.CharField(db_column='OwningAg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderindex = models.IntegerField(db_column='orderIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dms_list'


class EmergencyAction(models.Model):
    id = models.IntegerField(primary_key=True)
    action = models.CharField(db_column='Action', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'emergency_action'



class EquipmentName(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    cctv_dms_names = models.CharField(db_column='cctv_dms_names', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    affectedtype = models.CharField(db_column='AffectedType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    affectedtypeindex = models.IntegerField(db_column='AffectedTypeIndex', blank=True, null=True)  # Field name made lowercase.
    owningag = models.CharField(db_column='OwningAg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderindex = models.IntegerField(db_column='orderIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'equipment_name'


class EquipmentSystem(models.Model):
    id = models.IntegerField(primary_key=True)
    equipment_system = models.CharField(db_column='Equipment_System', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sorder = models.IntegerField(db_column='SOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'equipment_system'


class EquipmentTypeOfProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    type_of_problem = models.CharField(db_column='type_of_problem', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'equipment_type_of_problem'


class GeneralEvent(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gen_event = models.CharField(db_column='Gen_Event', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'general_event'


class HelpActionTaken(models.Model):
    actiontaken = models.CharField(db_column='ActionTaken', max_length=50, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'help_action_taken'


class HelpAssistType(models.Model):
    typeofasssist = models.CharField(db_column='TypeOfAsssist', max_length=50, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'help_assist_type'


class HelpHowNotified(models.Model):
    hownotified = models.CharField(db_column='HowNotified', max_length=50,primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'help_how_notified'


class Municipality(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    municipality = models.CharField(db_column='Municipality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.NullBooleanField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'municipality'


class NittecEmployee(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadmin = models.NullBooleanField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'nittec_employee'


class NonEmergencyAction(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'non_emergency_action'



class OwningAgency(models.Model):
    id = models.IntegerField(primary_key=True)
    member_agency = models.CharField(db_column='Member_Agency', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'owning_agency'


class Phonenumber(models.Model):
    phone_number = models.CharField(db_column='phone_number', max_length=50, primary_key=True)  # Field renamed to remove unsuitable characters.
    orderindex = models.IntegerField(db_column='orderIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'phonenumber'


class PvmsList(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nittec_name_crossroads_description = models.CharField(db_column='NITTEC_NAME_CROSSROADS_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner_id = models.CharField(db_column='OWNER_ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='LOCATION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project_id_description = models.CharField(db_column='PROJECT_ID_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    active = models.NullBooleanField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    show = models.NullBooleanField(db_column='SHOW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowxcol = models.CharField(db_column='ROWXCOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comp = models.CharField(db_column='COMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    software = models.CharField(db_column='SOFTWARE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_status = models.CharField(db_column='FIELD_STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner = models.CharField(db_column='OWNER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(db_column='MAKE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase1line1 = models.CharField(db_column='PHASE1LINE1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase1line2 = models.CharField(db_column='PHASE1LINE2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase1line3 = models.CharField(db_column='PHASE1LINE3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase2line1 = models.CharField(db_column='PHASE2LINE1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase2line2 = models.CharField(db_column='PHASE2LINE2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase2line3 = models.CharField(db_column='PHASE2LINE3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    controller_address = models.FloatField(db_column='CONTROLLER_ADDRESS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    public_name = models.CharField(db_column='PUBLIC_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    public_description = models.CharField(db_column='PUBLIC_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks = models.CharField(db_column='REMARKS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    match = models.CharField(db_column='Match', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crossroads_driven = models.NullBooleanField(db_column='CROSSROADS_DRIVEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'pvms_list'


class ReportingMemberAgency(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reporting_member_agency = models.CharField(db_column='Reporting_Member_Agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'reporting_member_agency'


class ReportingName(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reporting_name = models.CharField(db_column='Reporting_Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    active = models.NullBooleanField(blank=True, null=True)  # This field type is a guess.
    orderindex = models.IntegerField(db_column='orderIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reporting_name'


class RouteStreet(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    route_street = models.CharField(db_column='Route_Street', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'route_street'


class Signal(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    signal_problems = models.CharField(db_column='signal_problems', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'signal'


class TransitOperatorResponse(models.Model):
    id = models.IntegerField(primary_key=True)
    operator_response = models.CharField(db_column='Operator_Response', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'transit_operator_response'

