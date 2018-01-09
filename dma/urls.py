
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from .view_ems import WatermeterView,WatermeterBldView

import mptt_urls


urlpatterns = [
    url(r'^$',views.home,name='home'),


    url(r'^getmeter/(?P<loc>\d+)/$',WatermeterView.as_view()),
    url(r'^getmeter/(?P<loc>\d+)/(?P<bld>\d+)/$',WatermeterView.as_view()),
    #url(r'^some/(?P<slug>[\w-]+)/$',Modelclass.as_view()),
    
    url(r'^dma_manage/',views.dma_manage,name='dma_manage'),
    url(r'^dma_service/',views.dma_service,name='dma_service'),
    url(r'^dma_meter/',views.dma_meter,name='dma_meter'),
    url(r'^press_manager/',views.press_manager,name='press_manager'),
    url(r'^analy_config/',views.analy_config,name='analy_config'),
    url(r'^service_manager/',views.service_manager,name='service_manager'),
    url(r'^pipe_check/',views.pipe_check,name='pipe_check'),
    url(r'^report/',views.report,name='report'),
    url(r'^premium_apply/',views.premium_apply,name='premium_apply'),
    url(r'^press_value',views.press_value,name='press_value'),
    url(r'^getztree',views.getztree,name='getztree'),
    url(r'^wbalance/',views.wbalance,name='wbalance'),
    url(r'^wbalance_mon/(\w+)/$',views.wbalance_mon,name='wbalance_mon'),
    url(r'^wstasitc/',views.wstasitc,name='wstasitc'),
    url(r'^cut_base/',views.cut_base,name='cut_base'),
    url(r'^economize/',views.economize,name='economize'),
    url(r'^nightflow/',views.nightflow,name='nightflow'),
    url(r'^conv/',views.show_genres,name='show_genres'),
    url(r'^dma_summary/',views.dma_summary,name='dma_summary'),
    url(r'^chart/', views.chart,  name='demo'),
    url(r'^dma/(?P<path>.*)', mptt_urls.view(model='dma.models.ZoneTree', view='dma.views.sub_dma', slug_field='slug'),  name='sub_dma'),
    
    #url(r'^getmeter/(.+)',views.getmeter,name='getmeter'),
    url('tblfminfo/', views.TblfminfoList.as_view()),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)