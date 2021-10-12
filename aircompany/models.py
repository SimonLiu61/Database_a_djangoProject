from django.db import models

# Create your models here.
class Aircompany(models.Model):
    companyid = models.IntegerField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    admin = models.CharField(db_column='Admin', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AirCompany'


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

class Plane(models.Model):
    planeid = models.AutoField(db_column='PlaneID', primary_key=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='CompanyID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    planemodel = models.CharField(db_column='PlaneModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    npeople = models.IntegerField(db_column='NPeople', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plane'