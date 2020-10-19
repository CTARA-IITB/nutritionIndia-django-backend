from django.shortcuts import render
from rest_framework import viewsets         
from .serializers import IndicatorSerializer, IndicatorUnitSubgroupSerializer, SubgroupSerializer, UtDataSerializer, UtDatatimeSerializer, AreaEnSerializer, AreaEnDropSerializer, NiStDtbPolySerializer  
from .models import UtData, AreaEn, Indicator, IndicatorUnitSubgroup, Subgroup, Timeperiod, NiStDtbPoly    
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet  
from django.db.models import Q
from rest_framework.response import Response   
from rest_framework import status       

class DashboardView(ObjectMultipleModelAPIViewSet):  
  def get_querylist(self):
        indicator_list=Indicator.objects.filter(Q(classification=8)).values('indicator_id', 'indicator_name').order_by('indicator_order')
        area_list=AreaEn.objects.values('area_id', 'area_name')
        indicatorSelect=indicator_list[0].get('indicator_id')
        subgroup_list = IndicatorUnitSubgroup.objects.filter(Q(indicator_id=indicatorSelect)).select_related('subgroup').order_by('subgroup__subgroup_order')
        subgroupSelect= subgroup_list[0].subgroup_id    
        timeperiod_list=UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(area=1)).select_related('timeperiod').distinct().order_by('-timeperiod')
        timeperiodSelect= timeperiod_list[0].timeperiod_id
        
        querylist = (
            {'queryset': indicator_list, 'serializer_class': IndicatorSerializer},
            {'queryset': subgroup_list, 'serializer_class': IndicatorUnitSubgroupSerializer},
            {'queryset': timeperiod_list, 'serializer_class': UtDatatimeSerializer},
            {'queryset': area_list, 'serializer_class': AreaEnDropSerializer},
        )
        return querylist

class Tab1MapView(ObjectMultipleModelAPIViewSet):
    
    def get_querylist(self):
      # indicatorSelect = self.request.query_params.get('indicator', None) # query parameters
      # subgroupSelect = self.request.query_params.get('subgroup', None)
      # timeperiodSelect = self.request.query_params.get('timeperiod', None)
      # areaSelect = self.request.query_params.get('timeperiod', None)
        indicatorSelect = 12
        subgroupSelect = 6
        timeperiodSelect = 21
        areaSelect = None
        if(areaSelect != None):
            areaDetails=AreaEn.objects.filter(area_id=areaSelect).values('area_level','area_name')
            select_area_level = areaDetails[0].get('area_level')
            select_area_name = areaDetails[0].get('area_name')
            if select_area_level == 2:
                    area_geodata =  NiStDtbPoly.objects.all().filter(st_name=select_area_name)
                    select_area_data = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_parent_id=areaSelect)).select_related('area')
            elif select_area_level == 3:
                    area_parentid =AreaEn.objects.filter(area_id=areaSelect).value('area_parent_id')
                    area_parent_name= AreaEn.objects.filter(area_parent_id=area_parentid).value('area_name')
                    area_geodata = NiStDtbPoly.objects.all().filter(st_name=area_parent_name)
                    select_area_data = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_parent_id=area_parentid)).select_related('area')
     
            querylist = (
                    {'queryset': area_geodata, 'serializer_class': NiStDtbPolySerializer},
                    {'queryset': select_area_data, 'serializer_class': UtDataSerializer},
                )
        else:
            datalevel3 = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_level=3)).select_related('area')
            datalevel2 = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_level=2)).select_related('area')
            querylist = (
                    {'queryset': datalevel2.union(datalevel3), 'serializer_class': UtDataSerializer},
            )
        return querylist


class AreaView(viewsets.ModelViewSet):
  serializer_class = AreaEnSerializer
  queryset = AreaEn.objects.all()