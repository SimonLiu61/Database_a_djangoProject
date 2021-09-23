from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userage = models.CharField(db_column='UserAge', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useridentity = models.CharField(db_column='UserIdentity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'
