# -*- coding: utf-8 -*-

from django import forms
from .models import Wbalance,ZoneTree,DmaZone,Community,FlowShareDayTax,PressShareDayTax,Tblfminfo,Watermeter,HdbTianhouBig
import datetime
#from datetime import datetime

TITLE_CHOICES = (
('MR', 'Mr.'),
('MRS', 'Mrs.'),
('MS', 'Ms.'),
)

YEAR_CHOICES = ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020')

class FilterForm(forms.Form):
    simid=forms.CharField(label='SimID', max_length=100)
    user=forms.ModelChoiceField(queryset=Tblfminfo.objects.all())
    start_date=forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    end_date=forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    
    
class TblfminfoForm(forms.ModelForm):
    class Meta:
        model = Tblfminfo
        fields = ['username','simid']