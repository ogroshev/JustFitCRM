from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User

class JfTrainings(models.Model):
    id_training = models.AutoField(primary_key=True)
    id_client = models.IntegerField(unique=True, blank=True, null=True)
    id_trainer = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JF_trainings'

class JfClients(models.Model):
    id_client = models.ForeignKey(JfTrainings, models.DO_NOTHING, db_column='id_client', primary_key=True)
    phone = models.IntegerField(blank=True, null=True)
    id_body_size = models.IntegerField(unique=True, blank=True, null=True)
    column_4 = models.IntegerField(blank=True, null=True)
    id_gender = models.IntegerField(unique=True, blank=True, null=True)
    column_6 = models.IntegerField(blank=True, null=True)
    column_7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JF_clients'


class JfGender(models.Model):
    id_gender = models.ForeignKey(JfClients, models.DO_NOTHING, db_column='id_gender', primary_key=True)
    gender = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JF_gender'


class JfSizes(models.Model):
    id_size = models.AutoField(primary_key=True)
    size = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JF_sizes'


class JfTrainers(models.Model):
    id_client = models.IntegerField(primary_key=True)
    phone = models.IntegerField(blank=True, null=True)
    new_column = models.IntegerField(blank=True, null=True)
    column_4 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JF_trainers'



