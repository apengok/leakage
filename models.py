# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Branchnode(models.Model):
    nodeid = models.IntegerField(db_column='NodeId', primary_key=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=30)  # Field name made lowercase.
    energynodeid = models.IntegerField(db_column='EnergyNodeId', blank=True, null=True)  # Field name made lowercase.
    metermodelid = models.IntegerField(db_column='MeterModelId', blank=True, null=True)  # Field name made lowercase.
    maxload = models.CharField(db_column='MaxLoad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    monthlimit = models.CharField(db_column='MonthLimit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    meterbottomvalue = models.CharField(db_column='MeterBottomValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cumulativevalue = models.CharField(db_column='CumulativeValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    invalidstrdatetime = models.CharField(db_column='InvalidStrDateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    changedate = models.CharField(db_column='ChangeDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    parentnodeid = models.IntegerField(db_column='ParentNodeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branchnode'


class Branchnodeext(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    extname = models.CharField(db_column='ExtName', max_length=64)  # Field name made lowercase.
    exttag = models.CharField(db_column='ExtTag', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branchnodeext'
        unique_together = (('branchnodeid', 'extname'),)


class Building(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=30, blank=True, null=True)  # Field name made lowercase.
    airarea = models.CharField(db_column='AirArea', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'building'


class Emsparam(models.Model):
    paramkey = models.CharField(db_column='paramKey', primary_key=True, max_length=64)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='paramValue', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emsparam'


class Energynode(models.Model):
    nodeid = models.IntegerField(db_column='NodeId', primary_key=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=30)  # Field name made lowercase.
    energyflag = models.IntegerField(db_column='EnergyFlag', blank=True, null=True)  # Field name made lowercase.
    parentnodeid = models.IntegerField(db_column='ParentNodeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'energynode'


class HdbDay2015(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2015'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2016(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2016'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2017(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2017'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2018(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2018'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2019(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2019'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2020(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2020'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2021(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2021'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2022(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2022'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2023(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2023'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2024(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2024'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2025(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2025'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2026(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2026'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2027(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2027'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2028(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2028'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2029(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2029'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2030(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2030'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2031(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2031'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2032(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2032'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2033(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2033'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2034(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2034'
        unique_together = (('branchnodeid', 'date'),)


class HdbDay2035(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    meterzerovalue = models.CharField(db_column='MeterZeroValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_day_2035'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2015(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2015'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2016(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2016'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2017(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2017'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2018(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2018'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2019(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2019'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2020(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2020'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2021(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2021'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2022(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2022'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2023(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2023'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2024(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2024'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2025(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2025'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2026(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2026'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2027(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2027'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2028(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2028'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2029(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2029'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2030(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2030'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2031(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2031'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2032(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2032'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2033(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2033'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2034(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2034'
        unique_together = (('branchnodeid', 'date'),)


class HdbHour2035(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_hour_2035'
        unique_together = (('branchnodeid', 'date'),)


class HdbMonth(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_month'
        unique_together = (('branchnodeid', 'date'),)


class HdbQuarter(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_quarter'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2015(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2015'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2016(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2016'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2017(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2017'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2018(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2018'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2019(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2019'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2020(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2020'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2021(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2021'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2022(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2022'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2023(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2023'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2024(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2024'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2025(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2025'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2026(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2026'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2027(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2027'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2028(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2028'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2029(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2029'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2030(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2030'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2031(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2031'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2032(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2032'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2033(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2033'
        unique_together = (('branchnodeid', 'date'),)


class HdbSampling2034(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=20)
    volume = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    data_flag = models.IntegerField(blank=True, null=True)
    volume_type = models.IntegerField(blank=True, null=True)
    bottom_value = models.FloatField(blank=True, null=True)
    cumulative_value = models.FloatField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_sampling_2034'
        unique_together = (('branchnodeid', 'date'),)


class HdbWeek(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_week'
        unique_together = (('branchnodeid', 'date'),)


class HdbYear(models.Model):
    buildingid = models.IntegerField(db_column='BuildingId', blank=True, null=True)  # Field name made lowercase.
    branchnodeid = models.IntegerField(db_column='BranchNodeId', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    total = models.FloatField(blank=True, null=True)
    peak = models.FloatField(blank=True, null=True)
    flat = models.FloatField(blank=True, null=True)
    valley = models.FloatField(blank=True, null=True)
    total_fee = models.FloatField(blank=True, null=True)
    peak_fee = models.FloatField(blank=True, null=True)
    flat_fee = models.FloatField(blank=True, null=True)
    valley_fee = models.FloatField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdb_year'
        unique_together = (('branchnodeid', 'date'),)


class Metermodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metermodel'


class Timeblock(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    strhour = models.CharField(db_column='StrHour', max_length=30, blank=True, null=True)  # Field name made lowercase.
    endhour = models.CharField(db_column='EndHour', max_length=30, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeblock'


class Weather(models.Model):
    date = models.CharField(primary_key=True, max_length=10)
    humidity = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather'


class WeatherHour(models.Model):
    date = models.CharField(primary_key=True, max_length=20)
    humidity = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_hour'
