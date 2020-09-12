from django.db import models

# Model for construction projects page
class Project(models.Model):
    dnumber = models.CharField(max_length=20)
    road = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    objects = models.Manager()
    def __str__(self):
        return self.dnumber + " - " + self.description


