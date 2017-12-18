# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models
from django.utils.functional import lazy
from django.core.urlresolvers import reverse
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
        managed = False
        db_table = 'wbalance'

    def __unicode__(self):
        return '<Wbalance %s>'%(self.name)
        
    
class ZoneTree(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
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

    zone_name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    zone_area = models.FloatField(blank=True, null=True)
    zone_water_in = models.FloatField(blank=True, null=True)
    registed_user = models.FloatField(blank=True, null=True)
    pipeline_length = models.FloatField(blank=True, null=True)
    sub_zone_num = models.FloatField(blank=True, null=True)
    dma_num = models.FloatField(blank=True, null=True)
    measure_per_actual = models.FloatField(blank=True, null=True)
    measure_precision = models.FloatField(blank=True, null=True)
    zone_sale = models.FloatField(blank=True, null=True)
    nightflow_min = models.FloatField(blank=True, null=True)
    online_presspoint_num = models.FloatField(blank=True, null=True)
    online_flowmeter_num = models.FloatField(blank=True, null=True)
    online_water_quality_m_num = models.FloatField(blank=True, null=True)
    charge_watermeter_num = models.FloatField(blank=True, null=True)
    charge_waterwater_percent = models.FloatField(blank=True, null=True)
    zone_detect_leak_num = models.FloatField(blank=True, null=True)
    leak_water = models.FloatField(blank=True, null=True)
    leak_obscur_water = models.FloatField(blank=True, null=True)
    leak_obvious_water = models.FloatField(blank=True, null=True)
    leak_rate = models.FloatField(blank=True, null=True)
    pressure_quality = models.FloatField(blank=True, null=True)
    water_quality = models.FloatField(blank=True, null=True)
    zone_inner_pressure = models.FloatField(blank=True, null=True)

    #zone = models.ForeignKey(ZoneTree, on_delete=models.CASCADE,blank=True, null=True)
    zone = TreeForeignKey(ZoneTree, verbose_name='zone tree', related_name='dmazone',null=True, blank=True)
    slug = models.SlugField()

    class Meta:
        unique_together = ('slug', 'zone')
        db_table = 'dmazone'
        

