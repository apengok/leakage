# -*- coding: utf-8 -*-

from django import forms
from models import Wbalance,ZoneTree,DmaZone,Community,FlowShareDayTax,PressShareDayTax,Tblfminfo,Watermeter,HdbTianhouBig
import datetime
#from datetime import datetime

TITLE_CHOICES = (
('MR', 'Mr.'),
('MRS', 'Mrs.'),
('MS', 'Ms.'),
)

class FilterForm(forms.Form):
    simid=forms.CharField(label='SimID', max_length=100,widget=forms.Select(choices=TITLE_CHOICES),)
    user=forms.ModelChoiceField(queryset=Tblfminfo.objects.all())
    start_date=forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    end_date=forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    
    
class TblfminfoForm(forms.ModelForm):
    class Meta:
        model = Tblfminfo
        fields = ['username','simid']