# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from models import Wbalance,ZoneTree,DmaZone
from dma import dma_tree,dma_file,summary_file,static_monthly

import json
# Create your views here.
def index(request):
    return render(request,'dma/home.html')
    
def contact(request):
    return render(request, 'dma/home.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})
    
def wbalance(request):
    balance_all = Wbalance.objects.order_by('name').all()
    month_group = [ba.name for ba in balance_all ]
    
    context = {
        'current_mon':month_group[0],
        'month_group':month_group,
        'balance':balance_all[0]
    }
    
    
    
    return render(request,'dma/wbalance.html',context)

    
def wbalance_mon(request,mon):
    balance = Wbalance.objects.order_by('name').all()
    month_group = [ba.name for ba in balance ]
    balance1 = Wbalance.objects.get(name=mon)
    
    return render(request,'dma/wbalance.html',{'balance':balance1,'month_group':month_group,'current_mon':mon})

    
def wstasitc(request):
    balance = Wbalance.objects.order_by('name').all()
    month_group = [ba.name for ba in balance ]
    
    
    return render(request,'dma/wstasitc.html',{'balance':balance[0],'month_group':month_group,'current_mon':month_group[0],'static_monthly':static_monthly})
    
def economize(request):

    return render(request,'dma/economize.html')
    
    
def dma(request):
    
    #p_names = 
    
    dma_dist = {}
    def as_tree(na):
        
        zone_collections = ZoneTree.objects.filter(parent_level=na)
        for zone in zone_collections:
            p_name = zone.parent_level
            if p_name not in dma_dist.keys():
                tmp_ = {}
                tmp_['text'] = p_name
                tmp_['nodes'] = []
                dma_dist[p_name]=[]
                dma_dist[p_name].append(zone.zone_name)
            else:
                dma_dist[p_name].append(zone.zone_name)
            as_tree(zone.zone_name)
        #print dma_dist
        return dma_dist
    #return HttpResponse( json.dumps(as_tree('root') ))
    jds=json.dumps(as_tree('root'))
    print jds
    dma_file['zone_name']['value'] = dma_tree[0]['text'].decode('utf-8')
    return render(request,'dma/dma.html',{'json_data': jds,'dma_content':dma_file})
    
def sub_dma(request,fullurl):
    try:
        namelist = fullurl.split('/')
        if len(namelist) == 2:
            dma_name = namelist[1]
            dma_file.get('name')['value']=dma_name
        if len(namelist) == 3:
            dma_name = namelist[1]
            sub_name = namelist[2]
            dma_file.get('name')['value']=sub_name
        else:
            dma_file.get('name')['value']=namelist[-1]
        messages.add_message(request, messages.INFO, "you selected:%s"%(fullurl,))
        
    except :
        namelist = fullurl.split('/')
        messages.debug(request, "you selected:%s-%s"%(fullurl,' '.join(namelist)))
        messages.error(request, 'invalid dma name')
        
    #dma_file['name']['value'] = dma_name
    return render(request,'dma/dma.html',{'json_data':dma_tree,'dma_content':dma_file})

def dma_summary(request):
       
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render(request,'dma/dma_summary.html',{'json_data':dma_tree,'summary_content':summary_file})