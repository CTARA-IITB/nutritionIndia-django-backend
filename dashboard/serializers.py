from rest_framework import serializers
from .models import UtData


class UtDataSerializer(serializers.ModelSerializer):
    data_value= serializers.DecimalField(max_digits=255, decimal_places=3)
    class Meta:
        model = UtData
        fields = ('data_id','data_value')