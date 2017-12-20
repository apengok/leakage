from django.conf.urls import url
from . import views

import mptt_urls

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'dma/',views.dma,name='dma'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^wbalance/',views.wbalance,name='wbalance'),
    url(r'^wbalance_mon/(\w+)/$',views.wbalance_mon,name='wbalance_mon'),
    url(r'^wstasitc/',views.wstasitc,name='wstasitc'),
    url(r'^economize/',views.economize,name='economize'),
    url(r'^conv/',views.show_genres,name='show_genres'),
    url(r'^dma_summary/',views.dma_summary,name='dma_summary'),
    
    url(r'^dma/(?P<path>.*)', mptt_urls.view(model='dma.models.ZoneTree', view='dma.views.sub_dma', slug_field='slug'), {'extra': 'You may also pass extra options as usual!'}, name='sub_dma'),
    
    
]