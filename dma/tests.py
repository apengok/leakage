# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from dma.models import Wbalance,ZoneTree,DmaZone



class ZoneTreeTestCase(TestCase):
    def setUp(self):
        pass

    def test_zone(self):
        zone_collections = ZoneTree.objects.all()
        print zone_collections