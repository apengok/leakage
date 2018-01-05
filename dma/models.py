# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models
from django.utils.functional import lazy
#from django.core.urlresolvers import reverse
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Wbalance(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    totoal_in = models.FloatField(blank=True, null=True)
    auth_use = models.FloatField(blank=True, null=True)
    loss = models.FloatField(blank=True, null=True)
    charge_auth = models.FloatField(blank=True, null=True)
    uncharge_auth = models.FloatField(blank=True, null=True)
    charge_measure = models.FloatField(blank=True, null=True)
    charge_unmeasure = models.FloatField(blank=True, null=True)
    uncharge_measure = models.FloatField(blank=True, null=True)
    uncharge_unmeasure = models.FloatField(blank=True, null=True)
    apparent_loss = models.FloatField(blank=True, null=True)
    actual_loss = models.FloatField(blank=True, null=True)
    unauth_use = models.FloatField(blank=True, null=True)
    statistic_error = models.FloatField(blank=True, null=True)
    money_back = models.FloatField(blank=True, null=True)
    money_waste = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wbalance'

    def __unicode__(self):
        return '<Wbalance %s>'%(self.name)
        
    
class ZoneTree(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True)
    slug = models.SlugField()
    
    def get_absolute_url(self):
        return reverse('sub_dma', kwargs={'path': self.get_path()})

    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        
        unique_together = ('slug', 'parent')
        db_table = 'zonetree'
    

    def __unicode__(self):
        return self.name
        
    
        
    
 

class DmaZone(models.Model):
    dma_id = models.AutoField(primary_key=True)

    zone_name = models.CharField('分区名称',unique=True, max_length=64, blank=True, null=True)
    zone_area = models.FloatField('分区面积（平方公里）',blank=True, null=True)
    zone_water_in = models.FloatField('分区进水量（ m3）',blank=True, null=True)
    registed_user = models.FloatField('注册用户总数（万户）',blank=True, null=True)
    pipeline_length = models.FloatField('管线长度（ km）',blank=True, null=True)
    sub_zone_num = models.FloatField('下一级分区数量（个）',blank=True, null=True)
    dma_num = models.FloatField('分区中 DMA 数量（个）',blank=True, null=True)
    measure_per_actual = models.FloatField('水表抄见率（ %）',blank=True, null=True)
    measure_precision = models.FloatField('抄表准确率（ %）',blank=True, null=True)
    zone_sale = models.FloatField('分区销售水量（ m3）',blank=True, null=True)
    nightflow_min = models.FloatField('夜间最小流量（ m3）',blank=True, null=True)
    online_presspoint_num = models.FloatField('在线压力点数量（个）',blank=True, null=True)
    online_flowmeter_num = models.FloatField('在线流量计数量（个）',blank=True, null=True)
    online_water_quality_m_num = models.FloatField('在线水质监测点数量（个）',blank=True, null=True)
    charge_watermeter_num = models.FloatField('收费用远传水表数量（只）',blank=True, null=True)
    charge_waterwater_percent = models.FloatField('收费用远传水表水量占分区销 水量比（ %）',blank=True, null=True)
    zone_detect_leak_num = models.FloatField('分区探出漏点总数（个）',blank=True, null=True)
    leak_water = models.FloatField('漏失水量（ m3）',blank=True, null=True)
    leak_obscur_water = models.FloatField('暗漏水量（ m3）',blank=True, null=True)
    leak_obvious_water = models.FloatField('明漏水量（ m3）',blank=True, null=True)
    leak_rate = models.FloatField('漏损率（ %）',blank=True, null=True)
    pressure_quality = models.FloatField('压力合格率（ %）',blank=True, null=True)
    water_quality = models.FloatField('水质合格率（ %）',blank=True, null=True)
    zone_inner_pressure = models.FloatField('分区内压力（ MPa）',blank=True, null=True)

    #zone = models.ForeignKey(ZoneTree, on_delete=models.CASCADE,blank=True, null=True)
    zone = TreeForeignKey(ZoneTree, verbose_name='分区选择',on_delete=models.CASCADE, related_name='dmazone',null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        unique_together = ('slug', 'zone')
        db_table = 'dmazone'
        
    def __unicode__(self):
        return self.zone_name
        
class District(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'district'        
        
    def __unicode__(self):
        return self.name

class Community(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    metabinding = models.CharField(db_column='MetaBinding', max_length=20, blank=True, null=True)  # Field name made lowercase.
    districtid = models.IntegerField(db_column='DistrictId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'community'


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
        managed = True
        db_table = 'flow_share_day_tax'


class PressShareDayTax(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    readtime = models.CharField(db_column='ReadTime', max_length=20)  # Field name made lowercase.
    simid = models.CharField(db_column='SIMID', max_length=20)  # Field name made lowercase.
    pressure = models.FloatField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    warning = models.CharField(db_column='Warning', max_length=50)  # Field name made lowercase.
    warningdesc = models.CharField(db_column='WarningDesc', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
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
        managed = True
        db_table = 'tblfminfo'
        
    def __unicode__(self):
        return self.simid


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
        managed = True
        db_table = 'watermeter'
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
        managed = True
        db_table = 'hdb_tianhou_big'

