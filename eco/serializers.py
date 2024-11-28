from rest_framework import serializers
from .models import Ordenes,Puntos

class OrdenesSerializer(serializers.ModelSerializer):
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre')
    class Meta:
        model = Ordenes
        fields = '__all__'

class PuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntos
        fields = '__all__'