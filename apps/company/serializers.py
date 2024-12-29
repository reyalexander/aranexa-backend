from rest_framework import serializers
from .models import *

class CompanyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInformation
        fields = "__all__"


class CompanyBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBrand
        fields = "__all__"