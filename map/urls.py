from django.conf.urls import url
from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^getGeom',views.getGeom,name='getGeom'),
    
]