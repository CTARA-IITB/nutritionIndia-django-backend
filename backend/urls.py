from django.contrib import admin
from django.urls import path, include  
from dashboard.views import IndicatorListView, SubgroupListView, TimeperiodListView, AreaListView, IndiaMapView, AreaDataView, AreaMapView                                 


urlpatterns = [
    path('api/indicator', IndicatorListView.as_view(), name='indicator'),
    path('api/subgroup/<int:indicator>',  SubgroupListView.as_view(), name='subgroup'),
    path('api/timeperiod/<int:indicator>/<int:subgroup>/<int:area>', TimeperiodListView.as_view(), name='timeperiod'),
    path('api/area', AreaListView.as_view(), name='area'),
    path('api/indiaMap/<int:indicator>/<int:subgroup>/<int:timeperiod>/<int:area_level>', IndiaMapView.as_view(), name='indiaMap'),
    path('api/areaData', AreaDataView.as_view(), name='areaData'),
    path('api/areaMap', AreaMapView.as_view(), name='areaMap'),
]
