from rest_framework import serializers
from .models import UtData, AreaEn, Indicator, IndicatorUnitSubgroup, Subgroup, Timeperiod, NiStDtbPoly

class AreaEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaEn
        fields = ('area_id', 'area_code', 'area_name')

class AreaEnDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaEn
        fields = ('area_id', 'area_name')

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ('indicator_id','indicator_name')

class SubgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgroup
        fields = ('subgroup_id','subgroup_name')  

class TimeperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeperiod
        fields = ('timeperiod_id','timeperiod')

class IndicatorUnitSubgroupSerializer(serializers.ModelSerializer):
    subgroup = SubgroupSerializer()
    class Meta:
        model = IndicatorUnitSubgroup
        fields = ('subgroup',) 

class UtDatatimeSerializer(serializers.ModelSerializer):
    timeperiod = TimeperiodSerializer()
  
    class Meta:
        model = UtData
        fields = ('timeperiod',)

class UtDataSerializer(serializers.ModelSerializer):
    area = AreaEnSerializer()
    data_value = serializers.DecimalField(max_digits=255, decimal_places=2)
  
    class Meta:
        model = UtData
        fields = ('area' , 'data_value')

class NiStDtbPolySerializer(serializers.ModelSerializer):
    class Meta:
        model = NiStDtbPoly
        geo_field = "wkb_geometry"
        fields = ('id_field', 'st_name', 'dt_name')

# class UtDataSerializer(serializers.ModelSerializer):
#     data_value= serializers.DecimalField(max_digits=255, decimal_places=3)
#     class Meta:
#         model = UtData
#         fields = ('data_id','data_value')