# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib import messages

from django.views.generic import ListView
from .models import Wbalance,ZoneTree,DmaZone,District,Community,FlowShareDayTax,PressShareDayTax,Tblfminfo,Watermeter,HdbTianhouBig
from .dmadata import dma_tree,dma_file,summary_file,static_monthly
from .sidecontent import side_report,side_analy_config,side_dma_manage,side_dma_meter,side_dma_service,side_pipe_check,side_premium_apply,side_press_manage,side_service_manager
import json
import random
from datetime import datetime
from .forms import FilterForm

from .fusioncharts import FusionCharts

# Create your views here.

# The `chart` method is defined to load chart data from an JSON string.
def chart(request):
	# Create an object for the column2d chart using the FusionCharts class constructor
	column2d = FusionCharts("column2d", "ex2" , "600", "400", "chart-1", "json",
	 	# The data is passed as a string in the `dataSource` as parameter.
		"""{  
			   "chart": {  
				  "caption":"Harry\'s SuperMart",
				  "subCaption":"Top 5 stores in last month by revenue",
				  "numberPrefix":"$",
				  "theme":"ocean"
			   },
			   "data": [  
					{"label":"Bakersfield Central", "value":"880000"},
					{"label":"Garden Groove harbour", "value":"730000"},
					{"label":"Los Angeles Topanga", "value":"590000"},
					{"label":"Compton-Rancho Dom", "value":"520000"},
					{"label":"Daly City Serramonte", "value":"330000"}
				]
			}""")

	# returning complete JavaScript and HTML code, 
	# which is used to generate chart in the browsers.
	return  render(request, 'dma/home.html', {'output' : column2d.render()})

class TblfminfoList(ListView):
    model = Tblfminfo


def home(request):
    #messages.info(request,'home')
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            #simid = form.cleaned_data['simid']
            user = form.cleaned_data['user']
            
            started=form.cleaned_data['start_date']
            #ended=form.cleaned_data['end_date']
            flow_list=FlowShareDayTax.objects.filter(readtime__icontains=started).filter(simid=user.simid)
            #press_list=PressShareDayTax.objects.filter(readtime__range=[started,ended]).filter(simid=user.simid)
            
            # th_list=HdbTianhouBig
            # water_list=Watermeter
            # comty=Community
            #return HttpResponseRedirect('/dma/tblfminfo')
    else:
        form = FilterForm()
        flow_list=[]
        press_list=[]
        user = Tblfminfo.objects.all()[0]
    return render(request,'dma/home.html',{'form':form,'flow_list':flow_list,'user':user,'press_list':press_list})

#
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
    
    return render(request,'dma/dma_manage.html',{
        'dma_content':dma_file,
        'nodes':ZoneTree.objects.all(),
        'side_content':side_dma_manage})
        
def cut_base(request):
    return render(request,'dma/dma_manage/cut_base.html',{
        'dma_content':dma_file,
        'nodes':ZoneTree.objects.all(),
        'side_content':side_dma_manage})

def dma_service(request):
    return render(request,'dma/dma_service.html',
    {'side_content':side_dma_service})

def nightflow(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    flow_list=[]
    press_list=[]
    user = Tblfminfo.objects.all()[0]
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            
            user = form.cleaned_data['user']
            
            started=form.cleaned_data['start_date']
            print started,type(started)
            
            flow_list=FlowShareDayTax.objects.filter(readtime__icontains=started).filter(simid=user.simid)
            
            
            # th_list=HdbTianhouBig
            # water_list=Watermeter
            # comty=Community
            #return HttpResponseRedirect('/dma/tblfminfo')
    else:
        form = FilterForm()
        started="day"
        flow_list=[]
        press_list=[]
        user = Tblfminfo.objects.all()[0]
        
    if len(flow_list)>0:
        subc = flow_list[0].readtime[:10]
    else:
        subc = "day"
    cates = [{"label":v.readtime[11:]} for v in flow_list ]
    values0 = [{"value":10} for v in flow_list ]
    values = [{"value":v.flux} for v in flow_list ]
    datasource = {}
    datasource["chart"] = {
        "caption": "夜间最小流量",
        "subcaption": subc,
        "xaxisname": "Time",
        "yaxisname": "watermeter flow",
        "numberprefix": "$",
        "theme": "ocean"
    }
    datasource["categories"] = [{
        "category": cates
    }]

    datasource["dataset"] = [ {
            "seriesname": "flow ceiling",
            "renderas": "line",
            "showvalues": "0",
            "data": values0
        }, {
            "seriesname": "meter flow",
            "renderas": "line",
            "showvalues": "0",
            "data": values
        }
    ]
    column2d = FusionCharts("mscombi2d", "ex3" , "600", "400", "chart-1", "json",datasource)

    # returning complete JavaScript and HTML code, 
    # which is used to generate chart in the browsers.
    return  render(request, 'dma/nightflow.html', {
        'side_content':side_dma_service,
        'output' : column2d.render(),
        'form':form,
        'flow_list':flow_list,
        'user':user,
        'press_list':press_list})
    

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

def ems(request):
    pass
    
def press_value(request):
    if request.method == 'GET':
        id = request.GET.get('pid')
            
    if request.method == 'POST':
        id = request.POST.get('pid')
        
    
    pp=PressShareDayTax.objects.filter(pid=id)[0]
    sv_list={'lsl':random.randint(1,10),
        'cxc':random.randint(1,10),
        'dgc':random.randint(1,10),
        'jll':random.randint(1,10),
        'bll':random.randint(1,10),
        'nyl':pp.pressure,
        'dts':random.randint(1,10),}
    #results = [random.randint(1,10),]
    return JsonResponse({'press':sv_list})
    
def getztree(request):
    distris = District.objects.all()
    distris_list = [{'name':d.name} for d in distris]
    
    sub_dis = []
    for d in distris:
        tmp = {}
        tmp['name']=d.name
        comity = Community.objects.filter(districtid=d.id)
        tmp['children']=[]
        for c in comity:
            tmp1={}
            tmp1['name'] = c.name
            wt = Watermeter.objects.filter(communityid=c.id).distinct('buildingname')
            #wns = set([w.buildingname for w in wt])
            tmp1['url'] = "/dma/getmeter/"+str(c.id)
            tmp1['target'] = "_self"
            tmp1['children'] = [] #[{'name':s} for s in wns]
            for w in wt:
                tmp2 = {}
                tmp2['name'] = w.buildingname
                tmp2['url'] = "/dma/getmeter/{0}/{1}".format(str(c.id),w.id)
                tmp2['target'] = "_self"
                tmp1['children'].append(tmp2)
            tmp['children'].append(tmp1)
        #comity_list = [{'name':c.name} for c in comity]
        #tmp['children']=comity_list
        sub_dis.append(tmp)
        
    trees={'name':"歙县", 'open':'true', 'children':sub_dis}
    
    return JsonResponse({'trees':trees})


def getmeter(request,id):
    return JsonResponse({'id':id})
    
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

    return render(request,'dma/report/economize.html',{'side_content':side_report})
    
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
    
    
    return render(request,'dma/dma.html',{'dma_content':dma_file,'nodes':ZoneTree.objects.all(),'side_content':side_dma_manage})
    
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
    'dma_content':dma_file,
    'side_content':side_dma_manage})

def dma_summary(request):
       
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render(request,'dma/dma_summary.html',{
    'nodes':ZoneTree.objects.all(),'summary_content':summary_file})