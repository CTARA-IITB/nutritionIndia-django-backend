from rest_framework import serializers
from .models import UtData, AreaEn, Indicator, IndicatorUnitSubgroup, Subgroup, Timeperiod, NiStDtbPoly

class AreaEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaEn
        fields = ('area_id', 'area_code', 'area_name')

class AreaEnDropSerializer(serializers.ModelSerializer):
   # area_parent_id= serializers.DecimalField(max_digits=255, decimal_places=3)	
    # area_level= serializers.DecimalField(max_digits=255, decimal_places=3)
    value =  serializers.CharField(source='area_id')	#renaming and changing int to charfield
    label = serializers.CharField(source='area_name')	#renaming


    class Meta:	
        model = AreaEn	
        fields = ('value','label')	

    

class IndicatorSerializer(serializers.ModelSerializer):
    value =  serializers.CharField(source='indicator_id')	#renaming and changing int to charfield
    label = serializers.CharField(source='indicator_name')	#renaming

    class Meta:
        model = Indicator
        fields = ('value','label')	

class SubgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgroup
        fields = ('subgroup_id','subgroup_name')  

class TimeperiodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeperiod
        fields = ('timeperiod_id','timeperiod')

class IndicatorUnitSubgroupSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='subgroup.subgroup_id')
    label = serializers.CharField(source='subgroup.subgroup_name')

    class Meta:
        model = IndicatorUnitSubgroup
        fields = ('value','label')	

class UtDatatimeSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='timeperiod.timeperiod_id')
    label = serializers.CharField(source='timeperiod.timeperiod')
    class Meta:
        model = UtData
        fields = ('value','label')	

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