# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#
# class Aircompany(models.Model):
#     companyid = models.IntegerField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     admin = models.CharField(db_column='Admin', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'AirCompany'
#
#
# class Airport(models.Model):
#     airportid = models.AutoField(db_column='AirportID', primary_key=True)  # Field name made lowercase.
#     airportname = models.CharField(db_column='AirportName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Airport'
#
#
# class Flight(models.Model):
#     flightid = models.AutoField(db_column='FlightID', primary_key=True)  # Field name made lowercase.
#     planeid = models.ForeignKey('Plane', models.DO_NOTHING, db_column='PlaneID', blank=True, null=True)  # Field name made lowercase.
#     flightname = models.CharField(db_column='FlightName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     utime = models.DateTimeField(db_column='UTime', blank=True, null=True)  # Field name made lowercase.
#     dtime = models.DateTimeField(db_column='DTime', blank=True, null=True)  # Field name made lowercase.
#     origin = models.CharField(db_column='Origin', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isdelay = models.CharField(db_column='IsDelay', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Flight'
#
#
# class Plane(models.Model):
#     planeid = models.AutoField(db_column='PlaneID', primary_key=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(Aircompany, models.DO_NOTHING, db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
#     planemodel = models.CharField(db_column='PlaneModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     npeople = models.IntegerField(db_column='NPeople', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Plane'
#
#
# class Ticket(models.Model):
#     ticketid = models.AutoField(db_column='TicketID', primary_key=True)  # Field name made lowercase.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
#     flightid = models.ForeignKey(Flight, models.DO_NOTHING, db_column='FlightID', blank=True, null=True)  # Field name made lowercase.
#     airportid = models.ForeignKey(Airport, models.DO_NOTHING, db_column='AirportID', blank=True, null=True)  # Field name made lowercase.
#     money = models.CharField(db_column='Money', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'Ticket'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userage = models.CharField(db_column='UserAge', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useridentity = models.CharField(db_column='UserIdentity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'
