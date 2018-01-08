# -*- coding: utf-8 -*-
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
from django.views import View
from django.views.generic import TemplateView,ListView

class WatermeterView(ListView):
	template_name = 'dma/home.html'

	def get_queryset(self):
		print self.kwargs
		loc = self.kwargs.get('loc')
		if loc:
			queryset = Watermeter.objects.filter(communityid=int(loc))
		else:
			queryset = Watermeter.objects.none()
		return queryset
	
	def get_context_data(self,*args,**kwargs):
		print self.kwargs
		context = super(WatermeterView,self).get_context_data(*args,**kwargs)
		print context
		return context

	def get_object(self,*args,**kwargs):
		loc_id = self.kwargs.get("loc")
		obj = get_object_or_404(Watermeter,communityid=int(loc))
		return obj