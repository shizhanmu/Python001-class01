# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class QipaoshuiCleaned(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.ForeignKey(
        'StatTable', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    qptime = models.DateTimeField(blank=True, null=True)
    sentiment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'qipaoshui_cleaned'


class StatTable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stat_table'