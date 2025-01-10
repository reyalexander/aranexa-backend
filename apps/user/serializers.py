from rest_framework import serializers
from .models import *
from apps.client.serializers import ClientSerializer
from apps.company.serializers import CompanyBrandSerializer, CompanyInformationSerializer
from apps.product.serializers import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountSummarySerializer(serializers.ModelSerializer):
    # Relacionamos la info de Company, Brand y Client
    companyinformation_set = CompanyInformationSerializer(many=True, read_only=True)
    companybrand_set = CompanyBrandSerializer(many=True, read_only=True)
    client_set = ClientSerializer(many=True, read_only=True)
    product_set = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'full_name',
            'year_birthday',
            'gender',
            'level_of_study',
            # ... campos de Account ...
            'companyinformation_set',
            'companybrand_set',
            'client_set',
            'product_set',
        ]