from django.db import models

# Create your models here.

class Airport(models.Model):
    airportid = models.AutoField(db_column='AirportID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airportname = models.CharField(db_column='AirportName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Airport'


class Flight(models.Model):
    flightid = models.CharField(db_column='FlightID', primary_key=True, max_length=30)  # Field name made lowercase.
    planeid = models.IntegerField(db_column='PlaneID', blank=True, null=True)  # Field name made lowercase.
    flightname = models.CharField(db_column='FlightName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utime = models.CharField(db_column='UTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtime = models.CharField(db_column='DTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdelay = models.CharField(db_column='IsDelay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seatleft = models.IntegerField(db_column='SeatLeft', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'