# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    
