# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AlarmShareDayTax(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.CharField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    flux = models.FloatField(db_column='Flux', blank=True, null=True)  # Field name made lowercase.
    totalflux = models.FloatField(db_column='TotalFlux', blank=True, null=True)  # Field name made lowercase.
    pressure = models.FloatField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alarm_share_day_tax'


class Amrsparam(models.Model):
    paramkey = models.CharField(db_column='paramKey', primary_key=True, max_length=64)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='paramValue', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'amrsparam'


class Community(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.
    districtid = models.IntegerField(db_column='DistrictId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community'


class District(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'district'


class FlowShareDayTax(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.CharField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    flux = models.FloatField(db_column='Flux', blank=True, null=True)  # Field name made lowercase.
    plustotalflux = models.FloatField(db_column='PlusTotalFlux', blank=True, null=True)  # Field name made lowercase.
    reversetotalflux = models.FloatField(db_column='ReverseTotalFlux', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'flow_share_day_tax'


class GCloudlayer(models.Model):
    layername = models.CharField(db_column='LAYERNAME', primary_key=True, max_length=200)  # Field name made lowercase.
    tablename = models.CharField(db_column='TABLENAME', unique=True, max_length=200)  # Field name made lowercase.
    layerdesc = models.CharField(db_column='LAYERDESC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fastquery = models.IntegerField(db_column='FASTQUERY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer'


class GCloudlayerMetaHqcMapLayer(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_left = models.FloatField(db_column='BOUNDS_LEFT', blank=True, null=True)  # Field name made lowercase.
    bounds_top = models.FloatField(db_column='BOUNDS_TOP', blank=True, null=True)  # Field name made lowercase.
    bounds_right = models.FloatField(db_column='BOUNDS_RIGHT', blank=True, null=True)  # Field name made lowercase.
    bounds_bottom = models.FloatField(db_column='BOUNDS_BOTTOM', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_hqc_map_layer'


class GCloudlayerMetaNbL2(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_left = models.FloatField(db_column='BOUNDS_LEFT', blank=True, null=True)  # Field name made lowercase.
    bounds_top = models.FloatField(db_column='BOUNDS_TOP', blank=True, null=True)  # Field name made lowercase.
    bounds_right = models.FloatField(db_column='BOUNDS_RIGHT', blank=True, null=True)  # Field name made lowercase.
    bounds_bottom = models.FloatField(db_column='BOUNDS_BOTTOM', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_nb_l2'


class GCloudlayerMetaNoname1WsConcentrator(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_concentrator'


class GCloudlayerMetaNoname1WsConnector(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_connector'


class GCloudlayerMetaNoname1WsDrainValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_drain_valve'


class GCloudlayerMetaNoname1WsExEquipment(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_ex_equipment'


class GCloudlayerMetaNoname1WsFireHydrant(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_fire_hydrant'


class GCloudlayerMetaNoname1WsFlowMeter(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_flow_meter'


class GCloudlayerMetaNoname1WsForcePump(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_force_pump'


class GCloudlayerMetaNoname1WsMetabox(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_metabox'


class GCloudlayerMetaNoname1WsPipe(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_pipe'


class GCloudlayerMetaNoname1WsSourceWater(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_source_water'


class GCloudlayerMetaNoname1WsValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_valve'


class GCloudlayerMetaNoname1WsValveWell(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_valve_well'


class GCloudlayerMetaNoname1WsVentValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_vent_valve'


class GCloudlayerMetaNoname1WsWaterMeter(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_water_meter'


class GCloudlayerMetaNoname1WsWatermeterBasin(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_noname1_ws_watermeter_basin'


class GCloudlayerMetaSxGsWsConcentrator(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_concentrator'


class GCloudlayerMetaSxGsWsConnector(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_connector'


class GCloudlayerMetaSxGsWsDrainValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_drain_valve'


class GCloudlayerMetaSxGsWsExEquipment(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_ex_equipment'


class GCloudlayerMetaSxGsWsFireHydrant(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_fire_hydrant'


class GCloudlayerMetaSxGsWsFlowMeter(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_flow_meter'


class GCloudlayerMetaSxGsWsForcePump(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_force_pump'


class GCloudlayerMetaSxGsWsMetabox(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_metabox'


class GCloudlayerMetaSxGsWsPipe(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_pipe'


class GCloudlayerMetaSxGsWsSourceWater(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_source_water'


class GCloudlayerMetaSxGsWsValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_valve'


class GCloudlayerMetaSxGsWsValveWell(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_valve_well'


class GCloudlayerMetaSxGsWsVentValve(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_vent_valve'


class GCloudlayerMetaSxGsWsWaterMeter(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_water_meter'


class GCloudlayerMetaSxGsWsWatermeterBasin(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_gs_ws_watermeter_basin'


class GCloudlayerMetaSxQdzdtMapLayer(models.Model):
    metaid = models.IntegerField(db_column='METAID', primary_key=True)  # Field name made lowercase.
    metaname = models.CharField(db_column='METANAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bounds_size = models.FloatField(db_column='BOUNDS_SIZE', blank=True, null=True)  # Field name made lowercase.
    blockdata = models.TextField(db_column='BLOCKDATA', blank=True, null=True)  # Field name made lowercase.
    bounds_geom = models.TextField(db_column='BOUNDS_GEOM')  # Field name made lowercase. This field type is a guess.
    user_define = models.CharField(db_column='USER_DEFINE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'g_cloudlayer_meta_sx_qdzdt_map_layer'


class Hdb20160623173230(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_06_23_17_32_30'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160623180500(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_06_23_18_05_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160701040000(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_07_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160712040000(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_07_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160721040000(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_07_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160728171728(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_07_28_17_17_28'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160801040000(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hdb_2016_08_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160812040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_08_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160821040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_08_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160901040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_09_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20160921040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_09_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161001040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_10_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161012040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_10_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161021040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_10_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161101040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_11_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161112040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_11_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161121040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_11_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161201040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_12_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161212040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_12_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20161221040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2016_12_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170101040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170105083656(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_05_08_36_56'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170111171420(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_11_17_14_20'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170112040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170113140759(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_13_14_07_59'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170113143138(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_13_14_31_38'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170113155040(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_13_15_50_40'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170119163334(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_19_16_33_34'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170120093026(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_20_09_30_26'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170121040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170124152536(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_24_15_25_36'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170124152541(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_01_24_15_25_41'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170201040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_02_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170207093526(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_02_07_09_35_26'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170212040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_02_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170215171537(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_02_15_17_15_37'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170221040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_02_21_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170301040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_03_01_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170312040000(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_03_12_04_00_00'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170315140157(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_03_15_14_01_57'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Hdb20170315140201(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_2017_03_15_14_02_01'
        unique_together = (('nodeaddr', 'wateraddr'),)


class HdbTianhouBig(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    watermeterid = models.IntegerField(db_column='WaterMeterId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdb_tianhou_big'


class Hdbrecord(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    hdate = models.CharField(db_column='HDate', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hdbrecord'


class PressShareDayTax(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.CharField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    pressure = models.FloatField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'press_share_day_tax'


class Tblfminfo(models.Model):
    precinctname = models.CharField(db_column='PrecinctName', max_length=50)  # Field name made lowercase.
    filialename = models.CharField(db_column='FilialeName', max_length=50)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=20)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=50)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', primary_key=True, max_length=20)  # Field name made lowercase.
    fmtype = models.CharField(db_column='FMType', max_length=50)  # Field name made lowercase.
    fmaddress = models.CharField(db_column='FMAddress', max_length=20)  # Field name made lowercase.
    installdate = models.CharField(db_column='InstallDate', max_length=20)  # Field name made lowercase.
    install_jd = models.CharField(db_column='Install_JD', max_length=10)  # Field name made lowercase.
    install_wd = models.CharField(db_column='Install_WD', max_length=10)  # Field name made lowercase.
    updatetime = models.CharField(db_column='UpdateTime', max_length=20)  # Field name made lowercase.
    lastreadtime = models.CharField(db_column='LastReadTime', max_length=20)  # Field name made lowercase.
    lastflux = models.FloatField(db_column='LastFlux', blank=True, null=True)  # Field name made lowercase.
    lasttotalflux = models.FloatField(db_column='LastTotalFlux', blank=True, null=True)  # Field name made lowercase.
    lastpressure = models.FloatField(db_column='LastPressure', blank=True, null=True)  # Field name made lowercase.
    lastwarning = models.CharField(db_column='LastWarning', max_length=50)  # Field name made lowercase.
    lastwarningdesc = models.CharField(db_column='LastWarningDesc', max_length=20)  # Field name made lowercase.
    lastwarningtime = models.CharField(db_column='LastWarningTime', max_length=20)  # Field name made lowercase.
    lastreadpressuretime = models.CharField(db_column='LastReadPressureTime', max_length=20)  # Field name made lowercase.
    lastreadfluxtime = models.CharField(db_column='LastReadFluxTime', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfminfo'


class UserWatermeter(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    metering_equipment_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_watermeter'
        unique_together = (('nodeaddr', 'wateraddr'),)


class Watermeter(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numbersth = models.CharField(db_column='NumberSth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodeaddr = models.CharField(db_column='NodeAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wateraddr = models.CharField(db_column='WaterAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rvalue = models.CharField(db_column='RValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fvalue = models.CharField(db_column='FValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    metertype = models.CharField(db_column='MeterType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    meterstate = models.CharField(db_column='MeterState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrvalue = models.CharField(db_column='LastRValue', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastrtime = models.CharField(db_column='LastRTime', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    islargecalibermeter = models.IntegerField(db_column='IsLargeCaliberMeter', blank=True, null=True)  # Field name made lowercase.
    communityid = models.IntegerField(db_column='CommunityId', blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'watermeter'
        unique_together = (('nodeaddr', 'wateraddr'),)


class WsConcentrator(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    community = models.CharField(unique=True, max_length=128, blank=True, null=True)
    address = models.CharField(unique=True, max_length=128, blank=True, null=True)
    commdev = models.CharField(db_column='commDev', max_length=30, blank=True, null=True)  # Field name made lowercase.
    devaddr = models.CharField(db_column='devAddr', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commmodel = models.CharField(db_column='commModel', max_length=64, blank=True, null=True)  # Field name made lowercase.
    commparam = models.CharField(db_column='commParam', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(max_length=30, blank=True, null=True)
    netparam = models.CharField(db_column='netParam', max_length=30, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(max_length=32, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_concentrator'


class WsConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    item_type = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=128, blank=True, null=True)
    value_type = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=256, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)
    parentid = models.CharField(db_column='parentID', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ws_config'


class WsConnector(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_connector'


class WsDrainValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_drain_valve'


class WsExEquipment(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_ex_equipment'


class WsExResourceProperty(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    fieldname = models.CharField(max_length=128)
    fieldtype = models.IntegerField(blank=True, null=True)
    fieldlength = models.IntegerField(blank=True, null=True)
    caption = models.CharField(unique=True, max_length=128, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    mapping_column_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_ex_resource_property'
        unique_together = (('tablename', 'fieldname'),)


class WsExResourcePropertyEnumDefine(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    fieldname = models.CharField(max_length=128)
    enumvalue = models.IntegerField()
    enumcaption = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ws_ex_resource_property_enum_define'
        unique_together = (('tablename', 'fieldname', 'enumvalue'),)


class WsExResourceType(models.Model):
    tablename = models.CharField(primary_key=True, max_length=128)
    caption = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_ex_resource_type'


class WsFireHydrant(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_fire_hydrant'


class WsFlowMeter(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    simid = models.CharField(db_column='SIMID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_flow_meter'


class WsForcePump(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_force_pump'


class WsMetabox(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    buildingno = models.CharField(db_column='buildingNo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    concentrator_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_metabox'


class WsPipe(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    pipe_first = models.CharField(max_length=20, blank=True, null=True)
    pipe_end = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    buried = models.FloatField(blank=True, null=True)
    start_depth = models.FloatField(blank=True, null=True)
    end_depth = models.FloatField(blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    start_altitude = models.FloatField(blank=True, null=True)
    end_altitude = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_pipe'


class WsPipeType(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_pipe_type'


class WsProjectInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    number = models.CharField(max_length=64)
    project_name = models.CharField(max_length=255)
    manager_unit = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    completion_time = models.CharField(max_length=20, blank=True, null=True)
    measurement_unit = models.CharField(max_length=64, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    input_staff_id = models.CharField(max_length=32, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    minx = models.FloatField(blank=True, null=True)
    miny = models.FloatField(blank=True, null=True)
    maxx = models.FloatField(blank=True, null=True)
    maxy = models.FloatField(blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff_id = models.CharField(max_length=32, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_project_info'
        unique_together = (('id', 'number'),)


class WsProjectInfoExamineRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    op_user = models.CharField(max_length=32, blank=True, null=True)
    op_time = models.CharField(max_length=20, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    project_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ws_project_info_examine_record'


class WsProjectMeasurementRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    project_id = models.CharField(max_length=32)
    equipement_id = models.CharField(max_length=20)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ws_project_measurement_record'


class WsResource(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    tablename = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ws_resource'


class WsSourceWater(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_source_water'


class WsUserOpLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    op_user = models.CharField(max_length=255)
    op_mode = models.IntegerField(blank=True, null=True)
    is_current_op = models.IntegerField(blank=True, null=True)
    minx = models.FloatField(blank=True, null=True)
    miny = models.FloatField(blank=True, null=True)
    maxx = models.FloatField(blank=True, null=True)
    maxy = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    x1 = models.FloatField(blank=True, null=True)
    y1 = models.FloatField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    attr_id = models.CharField(max_length=32, blank=True, null=True)
    attr_tablename = models.CharField(db_column='attr_tableName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meta_id = models.CharField(max_length=32, blank=True, null=True)
    meta_tablename = models.CharField(db_column='meta_tableName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    op_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_user_op_log'


class WsValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_valve'


class WsValveWell(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_valve_well'


class WsVentValve(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_vent_valve'


class WsWaterMeter(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_water_meter'


class WsWatermeterBasin(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    input_time = models.CharField(max_length=20, blank=True, null=True)
    input_staff = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.CharField(max_length=20, blank=True, null=True)
    modify_staff = models.CharField(max_length=50, blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=256, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    caliber = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=256, blank=True, null=True)
    burying = models.CharField(max_length=256, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    road = models.CharField(max_length=256, blank=True, null=True)
    unit = models.CharField(max_length=256, blank=True, null=True)
    project_ref_count = models.IntegerField(blank=True, null=True)
    op_vaild = models.IntegerField(blank=True, null=True)
    project_no = models.CharField(max_length=256, blank=True, null=True)
    external_code = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_watermeter_basin'


class (models.Model):
    field_field = models.CharField(db_column='\u6237\u53f7', primary_key=True, max_length=30)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u6237\u540d', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u5730\u5740', max_length=128, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u8868\u8eab\u53f7', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u53e3\u5f84', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u8054\u7cfb\u7535\u8bdd', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u624b\u673a\u53f7\u7801', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u7528\u6237\u7c7b\u578b', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u6c34\u8868\u7528\u9014', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u5382\u5bb6\u540d\u79f0', max_length=128, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_9 = models.CharField(db_column='\u6c34\u8868\u578b\u53f7', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_10 = models.CharField(db_column='\u6c34\u8868\u7c7b\u578b', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_11 = models.CharField(db_column='\u6c34\u8868\u4f4d\u7f6e', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_12 = models.CharField(db_column='\u6284\u8868\u5468\u671f', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.CharField(db_column='\u4e0a\u671f\u6284\u8868\u65e5', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.CharField(db_column='\u4e0a\u671f\u884c\u81f3', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.CharField(db_column='\u672c\u671f\u6284\u8868\u65e5', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.CharField(db_column='\u672c\u671f\u884c\u81f3', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.CharField(db_column='\u65e7\u8868\u884c\u81f3', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.CharField(db_column='\u65b0\u8868\u884c\u81f3', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.CharField(db_column='\u5b9e\u7528\u6c34\u91cf', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.CharField(db_column='\u7528\u6237\u72b6\u6001', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.CharField(db_column='\u7528\u6c34\u72b6\u6001', max_length=30, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = '智慧水务平台调用用户信息'
