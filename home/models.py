from django.db import models


class open_event_logs(models.Model):
    log_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    route_street = models.CharField(max_length=50)
    general_event = models.CharField(max_length=50)
    event_description = models.CharField(max_length=50)

class open_construction_logs(models.Model):
    log_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    route_street = models.CharField(max_length=50)
    general_event = models.CharField(max_length=50)
    event_description = models.CharField(max_length=50)

class open_equipment_logs(models.Model):
    log_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    equiupment_system = models.CharField(max_length=20)
    equipment_name = models.CharField(max_length=20)
    type_of_problem = models.CharField(max_length=20)
    owning_agency = models.CharField(max_length=20)
    status =  models.CharField(max_length=20)