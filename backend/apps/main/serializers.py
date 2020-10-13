from rest_framework import serializers 
from .models import Producto
 
 
class WarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Producto
        fields = ('id_producto',
                  'nombre',
                  'descripcion')