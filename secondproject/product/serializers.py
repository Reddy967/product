from rest_framework import serializers
from .models import *

class productMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=producttMainModel
        fields='__all__'

class productImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields='__all__'