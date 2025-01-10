from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    client_type_display = serializers.SerializerMethodField()
    target_audience_display = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = ['id', 'client_type', 'client_type_display', 'target_audience', 'target_audience_display',
                  'recommendations', 'account_id']

    def get_client_type_display(self, obj):
        # Usa el método get_FIELD_display() del modelo para obtener el valor
        return obj.get_client_type_display()

    def get_target_audience_display(self, obj):
        # Usa el método get_FIELD_display() del modelo para obtener el valor
        return obj.get_target_audience_display()