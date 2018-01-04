# -*- coding: utf-8 -*-

from django import forms
from .models import Wbalance,ZoneTree,DmaZone,Community,FlowShareDayTax,PressShareDayTax,Tblfminfo,Watermeter,HdbTianhouBig
import datetime
#from datetime import datetime
from datetimewidget.widgets import DateWidget,DateTimeWidget


class FilterForm(forms.Form):
    #simid=forms.CharField(label='SimID', max_length=100)
    user=forms.ModelChoiceField(queryset=Tblfminfo.objects.all())
    start_date=forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    #end_date=forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    
    
class TblfminfoForm(forms.ModelForm):
    class Meta:
        model = Tblfminfo
        fields = ['username','simid']