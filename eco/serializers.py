from rest_framework import serializers
from .models import Ordenes,Puntos, Tiposmateriales

class TiposMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposmateriales
        fields = ['id', 'nombre']  # Incluye los campos que desees mostrar

class OrdenesSerializer(serializers.ModelSerializer):
    tipo = TiposMaterialesSerializer(read_only=True)
    class Meta:
        model = Ordenes
        fields = '__all__'

class PuntosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntos
        fields = '__all__'