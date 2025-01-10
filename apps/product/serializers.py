from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    product_name_display = serializers.SerializerMethodField()
    created_product_from_display = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_name_display', 
                  'product_description', 'created_product_from', 'created_product_from_display',
                  'product_invest', 'keep_product_track', 'price_appropiate', 'account_id']
    
    def get_product_name_display(self, obj):
        # Usa el método get_FIELD_display() del modelo para obtener el valor
        return obj.get_product_name_display()
    
    def get_created_product_from_display(self, obj):
        return obj.get_created_product_from_display()