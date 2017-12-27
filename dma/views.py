# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.contrib import messages

from models import Wbalance,ZoneTree,DmaZone,Community,FlowShareDayTax,PressShareDayTax,Tblfminfo,Watermeter,HdbTianhouBig
from dmadata import dma_tree,dma_file,summary_file,static_monthly
from .sidecontent import side_report,side_analy_config,side_dma_manage,side_dma_meter,side_dma_service,side_pipe_check,side_premium_apply,side_press_manage,side_service_manager
import json
# Create your views here.
def index(request):
    return render(request,'dma/home.html')
    
def dma_manage(request):
    dmz = DmaZone.objects.filter(zone_name='shenzhen').values()
    #dmz = get_object_or_404(DmaZone,zone=instance)
    #fields = DmaZone._meta.get_fields()
    try:
        for k,v in dmz[0].items():
            if k in dma_file.keys():
                dma_file[k]['value'] = v
    except:
        pass
    
    #dma_file['zone_name']['value'] = dma_tree[0]['text'].decode('utf-8')
    
    return render(request,'dma/dma_manage.html',{'dma_content':dma_file,'nodes':ZoneTree.objects.all(),
    'side_content':side_dma_manage})

def dma_service(request):
    return render(request,'dma/dma_service.html',
    {'side_content':side_dma_service})

def dma_meter(request):
    return render(request,'dma/dma_meter.html',
    {'side_content':side_dma_meter})

def press_manager(request):
    return render(request,'dma/press_manager.html',
    {'side_content':side_press_manage})

def analy_config(request):
    return render(request,'dma/analy_config.html',
    {'side_content':side_analy_config})

def service_manager(request):
    return render(request,'dma/service_manager.html',
    {'side_content':side_service_manager})

def pipe_check(request):
    return render(request,'dma/pipe_check.html',
    {'side_content':side_pipe_check})

def report(request):
    
    return render(request,'dma/report.html',
    {'side_content':side_report})

def premium_apply(request):
    return render(request,'dma/premium_apply.html',
    {'side_content':side_premium_apply})
    
def contact(request):
    return render(request, 'dma/home.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})
    
def wbalance(request):
    balance_all = Wbalance.objects.using('default').order_by('name').all()
    month_group = [ba.name for ba in balance_all ]
    
    context = {
        'current_mon':month_group[0],
        'month_group':month_group,
        'balance':balance_all[0],
        'side_content':side_report
    }
    
    
    
    return render(request,'dma/report/wbalance.html',context)

    
def wbalance_mon(request,mon):
    balance = Wbalance.objects.using('default').order_by('name').all()
    month_group = [ba.name for ba in balance ]
    balance1 = Wbalance.objects.using('default').get(name=mon)
    
    return render(request,'dma/report/wbalance.html',{'balance':balance1,'month_group':month_group,'current_mon':mon})

    
def wstasitc(request):
    balance = Wbalance.objects.using('default').order_by('name').all()
    month_group = [ba.name for ba in balance ]
    
    
    return render(request,'dma/report/wstasitc.html',{'balance':balance[0],'month_group':month_group,'current_mon':month_group[0],'static_monthly':static_monthly,'side_content':side_report})
    
def economize(request):

    return render(request,'dma/report/economize.html')
    
def show_genres(request):
    tmp = Community.objects.using('ems').all().values()
    return HttpResponse(tmp)
    #return render(request,"dma/includes/dmatree.html",
    #                      {'nodes':ZoneTree.objects.all()})
    
def dma(request):
    messages.info(request,'dma')
    dmz = DmaZone.objects.filter(zone_name='shenzhen').values()
    #dmz = get_object_or_404(DmaZone,zone=instance)
    #fields = DmaZone._meta.get_fields()
    try:
        for k,v in dmz[0].items():
            if k in dma_file.keys():
                dma_file[k]['value'] = v
    except:
        pass
    
    
    return render(request,'dma/dma.html',{'dma_content':dma_file,'nodes':ZoneTree.objects.all()})
    
def sub_dma(request,path,instance):
    
    #messages.info(request,'dma_sub')
    
    dmz = DmaZone.objects.filter(zone=instance).values()
    #dmz = get_object_or_404(DmaZone,zone=instance)
    #fields = DmaZone._meta.get_fields()
    try:
        for k,v in dmz[0].items():
            if k in dma_file.keys():
                dma_file[k]['value'] = v
    except:
        dma_file['zone_name']['value'] = instance.name
        
    
    
    return render(request,'dma/dma_manage.html',{
    'nodes':ZoneTree.objects.all(),
    'dma_content':dma_file})

def dma_summary(request):
       
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render(request,'dma/dma_summary.html',{
    'nodes':ZoneTree.objects.all(),'summary_content':summary_file})