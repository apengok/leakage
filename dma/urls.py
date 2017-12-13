from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^wbalance/',views.wbalance,name='wbalance'),
    url(r'^wbalance_mon/(\w+)/$',views.wbalance_mon,name='wbalance_mon'),
    url(r'^wstasitc/',views.wstasitc,name='wstasitc'),
    url(r'^economize/',views.economize,name='economize'),
    url(r'^dma/',views.dma,name='dma'),
    url(r'^dma_summary/',views.dma_summary,name='dma_summary'),
    #url(r'^sub_dma/(\w+)/',views.sub_dma,name='sub_dma'),
    
]