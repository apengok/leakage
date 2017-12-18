# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import ZoneTree,DmaZone

# Register your models here.

# class ZoneTreeForm(forms.ModelForm):
    
    # class Meta:
        # model = ZoneTree
        # exclude = ['href']
        
    # def __init__(self, *args, **kwargs):
        # super(ZoneTreeForm, self).__init__(*args, **kwargs)
        # zone_collections = ZoneTree.objects.all()
        # if len(zone_collections) == 0:
            # zone_choices = (('root','root'),)
        # else:
            # zone_choices = [ (o.zone_name, o.zone_name) for o in zone_collections]
        # self.fields['parent_level'] = forms.ChoiceField(choices=zone_choices)

# class ZoneTreeAdmin(admin.ModelAdmin):
    # fields = ('zone_level','zone_name','parent_level')

    # form = ZoneTreeForm


# admin.site.register(ZoneTree,ZoneTreeAdmin)

class ZoneTreeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name', )
    }
admin.site.register(ZoneTree, ZoneTreeAdmin)

class DmaZoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('zone_name', )
    }
admin.site.register(DmaZone, DmaZoneAdmin)

#admin.site.register(DmaZone)
#admin.site.register(ZoneTree, MPTTModelAdmin)