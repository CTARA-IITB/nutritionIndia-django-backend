
from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import UtDataSerializer      # add this
from .models import UtData                     # add this

class DashboardView(viewsets.ModelViewSet):       # add this
  serializer_class = UtDataSerializer          # add this
  queryset = UtData.objects.all()              # add this



# from django.shortcuts import render
# from .models import (AreaEn, Indicator,Tab1, Tab2, Tab3, Tab4, NiStDtbPoly, IndicatorUnitSubgroup, UtData)
# from django.views.generic import TemplateView
# from django.core import serializers
# from django.core.serializers import serialize
# from django.db.models import Q
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from .serializers import UtDataSerializer
# import json

# # Create your views here.

# class DashboardView(TemplateView):

# 	def get(self,request):
# 		areaSelect = request.GET.get('area')
# 		indicator_list=Indicator.objects.filter(Q(classification=8)).values('indicator_id', 'indicator_name').order_by('indicator_order')
# 		area_list=AreaEn.objects.values('area_id', 'area_name')
# 		indicatorSelect=indicator_list[0].get('indicator_id')
# 		area_geodata =[]
# 		select_area_data = []
# 		select_area_level = 1
# 		subgroup_list = IndicatorUnitSubgroup.objects.filter(Q(indicator_id=indicatorSelect)).select_related('subgroup').values('subgroup__subgroup_id', 'subgroup__subgroup_name').order_by('subgroup__subgroup_order')
# 		subgroupSelect= subgroup_list[0].get('subgroup__subgroup_id')
# 		if(areaSelect != None):
# 			timeperiod_list=UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(area=areaSelect)).select_related('timeperiod').values('timeperiod__timeperiod_id', 'timeperiod__timeperiod').distinct().order_by('-timeperiod')
# 			timeperiodSelect= timeperiod_list[0].get('timeperiod__timeperiod_id')
# 			areaDetails=AreaEn.objects.filter(area_id=areaSelect).values('area_level','area_name')
# 			select_area_level = areaDetails[0].get('area_level')
# 			select_area_name = areaDetails[0].get('area_name')
# 			if select_area_level == 2:
# 				area_geodata = serialize('geojson', NiStDtbPoly.objects.all().filter(st_name=select_area_name),
# 									geometry_field = 'wkb_geometry',
# 									fields = ('id','st_name','dt_name'))
# 				select_area_data = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_parent_id=areaSelect)).select_related('area').only('area__area_name', 'area__area_code', 'data_value')
# 			elif select_area_level == 3:
# 				area_parentid =AreaEn.objects.filter(area_id=areaSelect).value('area_parent_id')
# 				area_parent_name= AreaEn.objects.filter(area_parent_id=area_parentid).value('area_name')
# 				area_geodata = serialize('geojson', NiStDtbPoly.objects.all().filter(st_name=area_parent_name),
# 									geometry_field = 'wkb_geometry',
# 									fields = ('id','st_name','dt_name'))
# 				select_area_data = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_parent_id=area_parentid)).select_related('area').only('area__area_name', 'area__area_code', 'data_value')
# 		else:
# 			timeperiod_list=UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(area=1)).select_related('timeperiod').values('timeperiod__timeperiod_id', 'timeperiod__timeperiod').distinct().order_by('-timeperiod')
# 			timeperiodSelect= timeperiod_list[0].get('timeperiod__timeperiod_id')
		
# 		datalevel3 = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_level=3)).select_related('area').only('area__area_name', 'area__area_code', 'data_value')
# 		datalevel2 = UtData.objects.filter(Q(indicator=indicatorSelect) & Q(subgroup=subgroupSelect) & Q(timeperiod=timeperiodSelect) & Q(area__area_level=2)).select_related('area').only('area__area_name', 'area__area_code', 'data_value')
		
# 		jsondatalevel3= json.dumps(UtDataSerializer(datalevel3,  many=True).data)
# 		jsondatalevel2= json.dumps(UtDataSerializer(datalevel2,  many=True).data)
# 		jsonSelectAreaData = json.dumps(UtDataSerializer(select_area_data,  many=True).data)

# 		context = {
#             'data_level2': jsondatalevel2,
#             'data_level3': jsondatalevel3,
# 			'select_area_data' : jsonSelectAreaData,
# 			'select_area_geodata' : area_geodata
#         }
# 		return render(request,'map_dashboard/map.html', {'context':context, 'areaList': area_list ,'indicatorList': indicator_list,'subgroupList': subgroup_list, 'timeperiodList': timeperiod_list, 'area_level': select_area_level  })
	